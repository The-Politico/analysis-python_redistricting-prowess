# Imports from PROWESS.
from config import ALPHA_STRING
from config import BASE_TABLE_NAMES
from config import DISTRICT_ID_COLUMNS
from config import DISTRICT_NUMBER_COLUMNS
from config.divisions import DIVISIONS_FOR_STATE
from utils.db import load_state_with_db
from utils.sql_io import load_sql_file


def format_county_list(counties_raw):
    counties_list = ", ".join(
        [f"'{county_code}'" for county_code in counties_raw]
    )

    return f"( {counties_list} )"


def process_divisions(
    state_raw,
    district_type="old",
    db_shard="main_archive",
    partial_stage_one=None,
    plan_only=False,
):
    state_obj, shard_db, shard_cursor = load_state_with_db(state_raw)

    if not state_obj:
        return None, None, None

    state_abbr = state_obj.abbr.lower()

    all_divisions_in_state = DIVISIONS_FOR_STATE.get(state_abbr, ())

    if not all_divisions_in_state:
        print("ERROR: No divisions.")
        return None

    divisions_to_execute = list(all_divisions_in_state.keys())

    if partial_stage_one:
        if partial_stage_one in divisions_to_execute:
            divisions_to_execute = [partial_stage_one]
        else:
            print(f"ERROR: Division '{partial_stage_one}' not found.")
            return None

    division_template = load_sql_file(
        "queries/v1/001__divisions-to-execute.sql"
    )

    all_division_scripts = {}

    for division in divisions_to_execute:
        print(f"Milling division '{division}'...")

        division_values = all_divisions_in_state[division]

        division_script = f"{division_template}"

        group_operator = "IS NOT NULL"
        group_counties_list = ""
        if type(division_values) in [list, tuple]:
            group_operator = "IN"
            group_counties_list = format_county_list(division_values)
        elif division_values == "misc":
            group_operator = "NOT IN"

            all_named_counties = [
                county
                for slug, counties in all_divisions_in_state.items()
                if slug != division
                for county in counties
            ]

            group_counties_list = format_county_list(all_named_counties)

        group_letter = ALPHA_STRING[
            list(all_divisions_in_state).index(division)
        ]

        district_num_column = (
            DISTRICT_NUMBER_COLUMNS["old_districts"]
            if district_type == "old"
            else DISTRICT_NUMBER_COLUMNS["new_districts"]
        )
        division_script = division_script.replace(
            "{{{ district_num_column }}}", district_num_column
        )

        district_id_column = (
            DISTRICT_ID_COLUMNS["old_districts"]
            if district_type == "old"
            else DISTRICT_ID_COLUMNS["new_districts"]
        )
        division_script = division_script.replace(
            "{{{ district_id_column }}}", district_id_column
        )

        district_shape_table = (
            BASE_TABLE_NAMES["old_districts"]
            if district_type == "old"
            else BASE_TABLE_NAMES["new_districts"]
        )
        division_script = division_script.replace(
            "{{{ district_shape_table }}}", district_shape_table
        )

        division_script = division_script.replace(
            "{{{ group_operator }}}", group_operator
        )
        division_script = division_script.replace(
            "{{{ group_counties_list }}}", group_counties_list
        )
        division_script = division_script.replace(
            "{{{ group_suffix }}}", division
        )
        division_script = division_script.replace(
            "{{{ group_letter }}}", group_letter
        )

        if not plan_only:
            shard_cursor.execute(division_script)

        all_division_scripts[division] = division_script

        print("    Division done!")

    return all_division_scripts
