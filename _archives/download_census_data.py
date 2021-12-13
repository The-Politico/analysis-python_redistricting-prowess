# Imports from python.
import csv
import os
from pathlib import Path


# Imports from other dependencies.
import requests
import us


API_ROOT = "https://api.census.gov/data"

CENSUS_API_KEY = os.environ["CENSUS_API_KEY"]

FIELDS_TO_EXCLUDE = ["state", "county", "tract"]

REQUESTS_SESSION = requests.Session()


def get_acs_api_url(dataset_slug, columns_to_fetch, fips_code):
    joined_columns = ",".join(columns_to_fetch)

    return "".join(
        [
            f"{API_ROOT}/{dataset_slug}",
            f"?get={joined_columns}",
            "&for=tract:*",
            f"&in=state:{fips_code}",
            # f"&key={CENSUS_API_KEY}",
        ]
    )


def acs_to_dicts(dataset_slug, columns_to_fetch, fips_code):
    api_url = get_acs_api_url(dataset_slug, columns_to_fetch, fips_code)

    rq = requests.Request("GET", api_url).prepare()
    request_result = REQUESTS_SESSION.send(rq)

    table_contents = request_result.json()

    return [
        {
            table_contents[0][field_pos]: field_val
            for field_pos, field_val in enumerate(data_row)
            if table_contents[0][field_pos] not in FIELDS_TO_EXCLUDE
        }
        for data_row in table_contents[1:]
    ]


def export_acs_dicts(census_dicts, output_dir):
    # Create the output dir.
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    output_filename = f"{output_dir}/auto_gen.csv"

    with open(output_filename, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=census_dicts[0].keys())

        writer.writeheader()

        for data_row in census_dicts:
            writer.writerow(data_row)

    return output_filename


def download_racial_breakdowns():
    all_created_files = []

    for state in us.states.STATES:
        print(f"  > Downloading data for {state.name}...")

        dataset_slug = "2019/acs/acs5"

        columns_to_fetch = [
            "GEO_ID",
            "B03002_001E",
            "B03002_001M",
            "B03002_003E",
            "B03002_003M",
        ]

        census_dicts = acs_to_dicts(dataset_slug, columns_to_fetch, state.fips)

        output_dir = f"raw_data/census_race_plus_hl/{state.fips}"

        created_file = export_acs_dicts(census_dicts, output_dir)

        print("    √ DONE.")
        print("")

        all_created_files.append(created_file)

    return all_created_files


def download_educational_breakdowns():
    all_created_files = []

    for state in us.states.STATES:
        print(f"  > Downloading data for {state.name}...")

        dataset_slug = "2019/acs/acs5/subject"

        columns_to_fetch = [
            "GEO_ID",
            "S1501_C01_006E",
            "S1501_C01_006M",
            "S1501_C01_015E",
            "S1501_C01_015M",
        ]

        census_dicts = acs_to_dicts(dataset_slug, columns_to_fetch, state.fips)

        output_dir = f"raw_data/census_education_level/{state.fips}"

        created_file = export_acs_dicts(census_dicts, output_dir)

        print("    √ DONE.")
        print("")

        all_created_files.append(created_file)

    return all_created_files
