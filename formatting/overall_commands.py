# Imports from python.
from datetime import datetime
import json
import os


# Imports from other dependencies.
import pytz
import requests
import us


# Imports from PROWESS.
from config.storage import BASE_FILE_PATH
from config.storage import S3_BUCKET_NAME
from config.storage import S3_CLIENT
from config.storage import UPLOADED_FILES_ACL
from config.storage import UPLOADED_FILES_CACHE_HEADER
from formatting.state_detail import generate_state_file


KITCHENSINK_BASE_URL = (
    "https://www.politico.com/interactives/apps/kitchensink/forms"
)

KITCHENSINK_FORM_ID = os.environ["KITCHENSINK_FORM_ID"]

STATE_SUMMARY_URL = "".join(
    [
        "https://www.politico.com/interactives/2021/",
        "redistricting-tracker-data/stateSummary.json",
    ]
)


def generate_kitchensink_url():
    return f"{KITCHENSINK_BASE_URL}/{KITCHENSINK_FORM_ID}/data.json"


def get_instant_timestamp():
    local_time = pytz.timezone("America/New_York")

    naive_datetime = datetime.now()
    local_datetime = local_time.localize(naive_datetime)

    utc_datetime = local_datetime.astimezone(pytz.utc)
    iso_formatted = utc_datetime.isoformat()

    return iso_formatted.replace("+00:00", "Z")


def flatten_districts(timeframe_dict):
    if not timeframe_dict or not timeframe_dict.get("districts", None):
        return None

    return sorted(
        [
            district_dict["bidenMargin"]
            for district_number, district_dict in timeframe_dict[
                "districts"
            ].items()
        ]
    )


def format_promos(raw_promo_list):
    return [
        {key: val for key, val in promo_config.items() if key not in ["id"]}
        for promo_config in raw_promo_list
    ]


def format_state_summary(raw_state_detail):
    return dict(
        whoControls=raw_state_detail["whoControls"],
        mapProgress=raw_state_detail["mapProgress"],
        bidenMargins=dict(
            old=flatten_districts(raw_state_detail["oldMap"]),
            new=flatten_districts(raw_state_detail["newMap"]),
        ),
        partisanBenefit=raw_state_detail["partisanBenefit"],
    )


def load_state_summary():
    timestamp = int(datetime.utcnow().timestamp())

    state_summary_response = requests.get(f"{STATE_SUMMARY_URL}?t={timestamp}")

    return state_summary_response.json()


def fetch_summary_fields(state_summaries, state_fips):
    summary_for_state = state_summaries.get(state_fips, {})

    if not summary_for_state:
        return {}

    return dict(
        whoControls=summary_for_state["whoControls"],
        mapProgress=summary_for_state["mapProgress"],
        bidenMargins=summary_for_state["bidenMargins"],
    )


def rebake_single_state(state_raw):
    files_to_write = {}

    current_timestamp = get_instant_timestamp()

    imported_state_summary = load_state_summary()

    state_obj = us.states.lookup(state_raw)

    kitchensink_url = generate_kitchensink_url()
    kitchensink_response = requests.get(kitchensink_url)
    kitchensink_json = kitchensink_response.json()

    states_list = kitchensink_json["content"]["states"]

    states_dict = {
        state_config["state"]: {
            key: val
            for key, val in state_config.items()
            if key not in ["id", "state"]
        }
        for state_config in states_list
    }

    updated_state_file = generate_state_file(
        current_timestamp, states_dict, state_obj.fips
    )

    state_file_path = f"stateDetail_{state_obj.fips}"

    files_to_write[state_file_path] = updated_state_file

    # Re-bake stateSummary file with this state config included.
    updated_state_summary = dict(**imported_state_summary)
    # print(updated_state_summary.keys())
    updated_state_summary[state_obj.fips] = format_state_summary(
        updated_state_file
    )
    # print(updated_state_summary.keys())

    files_to_write["stateSummary"] = updated_state_summary

    # Re-bake global file, always.
    files_to_write["global"] = dict(
        promo=format_promos(kitchensink_json["content"]["promos"]),
        subtitles=kitchensink_json["content"]["subtitles"],
        keyStates={
            state_dict["state"]: dict(
                cardText=state_dict["keyState"],
                **fetch_summary_fields(
                    updated_state_summary, state_dict["state"]
                ),
            )
            for state_dict in kitchensink_json["content"]["states"]
            if state_dict.get("keyState", None)
        },
        lastUpdated=current_timestamp,
    )

    # TODO: Write out all files_to_write values.
    for filename, file_contents in files_to_write.items():
        S3_CLIENT.put_object(
            Body=json.dumps(file_contents),
            Bucket=S3_BUCKET_NAME,
            Key=f"{BASE_FILE_PATH}/{filename}.json",
            ACL=UPLOADED_FILES_ACL,
            CacheControl=UPLOADED_FILES_CACHE_HEADER,
            ContentType="application/json",
        )

    return files_to_write
