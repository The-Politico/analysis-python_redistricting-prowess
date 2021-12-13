# Imports from PROWESS.
from config import BASE_TABLE_NAMES
from config import DISTRICT_ID_COLUMNS
from config import DISTRICT_NUMBER_COLUMNS
from utils.db import load_state_with_db
from utils.sql_io import load_sql_file


def process_tract_coverage(
    state_raw,
    district_type="old",
    plan_only=False,
):
    state_obj, shard_db, shard_cursor = load_state_with_db(
        state_raw, "main_archive", "census"
    )

    if not state_obj:
        return None, None, None

    division_script = load_sql_file("queries/v1/101__tract-coverage.sql")

    print("Calculating tract coverage...")

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

    if not plan_only:
        shard_cursor.execute(division_script)

    return dict(all=division_script)
