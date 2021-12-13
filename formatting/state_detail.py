# Imports from other dependencies.
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists
import us


# Imports from PROWESS.
from config.db_configs import DB_CONFIGS
from config.precursors import DISTRICT_PRECURSORS


DATABASE_URL = DB_CONFIGS["main_archive"]

EMPTY_DATAFRAME = pd.DataFrame()


def load_sql_table_as_dataframe(database_name, table_name):
    full_db_string = f"{DATABASE_URL}/{database_name}"

    if not database_exists(full_db_string):
        print(f"INFO: Database '{table_name}' not found; skipping...")
        return EMPTY_DATAFRAME

    engine = create_engine(full_db_string)

    if table_name not in engine.table_names():
        print(f"ERROR: Table '{table_name}' not found.")
        return EMPTY_DATAFRAME

    return pd.read_sql_query(f'select * from "{table_name}"', con=engine)


def get_table_name(raw_data_type):
    if raw_data_type == "census":
        return "106__compared_margins"
    elif raw_data_type == "voting":
        return "007__compared_margins"

    return "0_0"


def load_state_data(state_abbr):
    db_names = dict(
        old=dict(
            census=f"prowess_v1_old__{state_abbr}__census",
            voting=f"prowess_v1_old__{state_abbr}",
        ),
        new=dict(
            census=f"prowess_v1_new__{state_abbr}__census",
            voting=f"prowess_v1_new__{state_abbr}",
        ),
    )

    dataframes_for_state = {
        timeframe: {
            data_type: load_sql_table_as_dataframe(
                database_name, get_table_name(data_type)
            )
            for data_type, database_name in timeframe_dict.items()
        }
        for timeframe, timeframe_dict in db_names.items()
    }

    return dataframes_for_state


def get_extra_per_district_fields(precursor_dict, district_number):
    if precursor_dict is not None:
        return dict(precursor=precursor_dict.get(district_number, None))
    return {}


def format_districts(timeframe_dict, year_int, precursor_dict=None):
    census_data = timeframe_dict.get("census", EMPTY_DATAFRAME)
    voting_data = timeframe_dict.get("voting", EMPTY_DATAFRAME)

    if census_data.empty or voting_data.empty:
        return None

    census_records = census_data.to_dict("records")
    census_dict = {
        district_row["district"]: dict(
            pctWithBachelors=round(
                district_row["bachelors_proportional95"] / 100, 4
            ),
            pctNonwhite=round(
                district_row["nonwhite_proportional95"] / 100, 4
            ),
        )
        for district_row in census_records
    }

    voting_records = voting_data.to_dict("records")
    voting_dict = {
        district_row["district"]: dict(
            year=year_int,
            bidenMargin=round(district_row["biden_proportional95"] / 100, 4),
        )
        for district_row in voting_records
    }

    shared_district_keys = sorted(
        list(set(census_dict.keys()).intersection(set(voting_dict.keys())))
    )

    return {
        district_number: dict(
            **voting_dict.get(district_number, {}),
            **census_dict.get(district_number, {}),
            **get_extra_per_district_fields(precursor_dict, district_number),
        )
        for district_number in shared_district_keys
    }


def generate_state_file(current_timestamp, kitchensink_states, state_raw):
    state_obj = us.states.lookup(state_raw)

    state_abbr = state_obj.abbr.lower()

    state_data = load_state_data(state_abbr)

    state_copy = kitchensink_states[state_obj.fips]

    state_adoption_date = state_copy.get("adoptionDate", None)

    map_progress_value = "adopted" if state_adoption_date else "inProgress"

    old_map_values = dict(districts=format_districts(state_data["old"], 2020))
    new_map_values = dict(
        districts=format_districts(
            state_data["new"], 2022, DISTRICT_PRECURSORS.get(state_abbr, {})
        )
    )

    if state_adoption_date:
        new_map_values["adoptionDate"] = state_adoption_date

    formatted_data = dict(
        fips=state_obj.fips,
        whoControls=state_copy.get("whoControls", None),
        mapProgress=map_progress_value,
        contextOverride=state_copy.get("contextOverride", None),
        swapNote=state_copy.get("swapNote", None),
        keyStateBacmText=state_copy.get("keyStateBacmText", None),
        oldMap=old_map_values,
        newMap=new_map_values,
        partisanBenefit=state_copy.get("partisanBenefit", None),
        lastUpdated=current_timestamp,  # "2021-11-16T15:56:17.199Z"
    )

    return formatted_data
