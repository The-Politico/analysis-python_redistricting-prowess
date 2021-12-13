# Imports from python.
import time


# Imports from PROWESS.
from analysis.political.data_prep import prepare_data
from analysis.political.division_processing import process_divisions
from analysis.political.merging import merge_divisions
from config import BASE_TABLE_NAMES
from config import DISTRICT_ID_COLUMNS
from config import DISTRICT_NUMBER_COLUMNS
from utils.db import load_state_with_db
from utils.sql_io import load_sql_file


def run_prep(state_raw, district_type, plan_only=False):
    start = time.time()
    prepare_data(state_raw, district_type, plan_only=plan_only)
    end = time.time()

    return end - start, []


def run_division(state_raw, district_type, division=None, plan_only=False):
    start = time.time()
    sts = process_divisions(
        state_raw, district_type, "main_archive", division, plan_only=plan_only
    )
    end = time.time()

    return end - start, sts


def run_merge(state_raw, plan_only=False):
    start = time.time()
    queries = merge_divisions(state_raw, "main_archive", plan_only=plan_only)
    end = time.time()

    return end - start, queries


def run_join(state_abbr, cursor, plan_only=False):
    all_queries = []

    start = time.time()

    join_script = load_sql_file("queries/v1/003__with-results.sql")
    if not plan_only:
        cursor.execute(join_script)
    all_queries.append(join_script)

    end = time.time()

    return end - start, all_queries


def run_calculation(state_abbr, cursor, plan_only=False):
    all_queries = []

    start = time.time()

    gather_script = load_sql_file("queries/v1/004a__majorities-only.sql")
    if not plan_only:
        cursor.execute(gather_script)
    all_queries.append(gather_script)

    cull_script = load_sql_file("queries/v1/004b__significant-minorities.sql")
    if not plan_only:
        cursor.execute(cull_script)
    all_queries.append(cull_script)

    group_script = load_sql_file("queries/v1/004c__grouped-minorities.sql")
    if not plan_only:
        cursor.execute(group_script)
    all_queries.append(group_script)

    gwt_script = load_sql_file("queries/v1/004d__grouped_with_threshold.sql")
    if not plan_only:
        cursor.execute(gwt_script)
    all_queries.append(gwt_script)

    thld1_script = load_sql_file("queries/v1/004e__main-count-90-percent.sql")
    if not plan_only:
        cursor.execute(thld1_script)
    all_queries.append(thld1_script)

    thld2_script = load_sql_file("queries/v1/004f__main-count-95-percent.sql")
    if not plan_only:
        cursor.execute(thld2_script)
    all_queries.append(thld2_script)

    thld3_script = load_sql_file("queries/v1/004g__main-count-97-percent.sql")
    if not plan_only:
        cursor.execute(thld3_script)
    all_queries.append(thld3_script)

    end = time.time()

    return end - start, all_queries


def run_assembly(state_abbr, cursor, plan_only=False):
    all_queries = []

    start = time.time()

    lcw_script = load_sql_file("queries/v1/005a__larger-coverage-wins.sql")
    if not plan_only:
        cursor.execute(lcw_script)
    all_queries.append(lcw_script)

    thld1_script = load_sql_file("queries/v1/005b__threshold-90-percent.sql")
    if not plan_only:
        cursor.execute(thld1_script)
    all_queries.append(thld1_script)

    thld2_script = load_sql_file("queries/v1/005c__threshold-95-percent.sql")
    if not plan_only:
        cursor.execute(thld2_script)
    all_queries.append(thld2_script)

    thld3_script = load_sql_file("queries/v1/005d__threshold-97-percent.sql")
    if not plan_only:
        cursor.execute(thld3_script)
    all_queries.append(thld3_script)

    pptn1_script = load_sql_file(
        "queries/v1/005e__proportional-90-percent.sql"
    )
    if not plan_only:
        cursor.execute(pptn1_script)
    all_queries.append(pptn1_script)

    pptn2_script = load_sql_file(
        "queries/v1/005f__proportional-95-percent.sql"
    )
    if not plan_only:
        cursor.execute(pptn2_script)
    all_queries.append(pptn2_script)

    pptn3_script = load_sql_file(
        "queries/v1/005g__proportional-97-percent.sql"
    )
    if not plan_only:
        cursor.execute(pptn3_script)
    all_queries.append(pptn3_script)

    end = time.time()

    return end - start, all_queries


def run_formatting(state_abbr, cursor, plan_only=False):
    all_queries = []

    start = time.time()

    lcw_script = load_sql_file("queries/v1/006a__larger-coverage-wins.sql")
    if not plan_only:
        cursor.execute(lcw_script)
    all_queries.append(lcw_script)

    thld1_script = load_sql_file("queries/v1/006b__threshold-90-percent.sql")
    if not plan_only:
        cursor.execute(thld1_script)
    all_queries.append(thld1_script)

    thld2_script = load_sql_file("queries/v1/006c__threshold-95-percent.sql")
    if not plan_only:
        cursor.execute(thld2_script)
    all_queries.append(thld2_script)

    thld3_script = load_sql_file("queries/v1/006d__threshold-97-percent.sql")
    if not plan_only:
        cursor.execute(thld3_script)
    all_queries.append(thld3_script)

    pptn1_script = load_sql_file(
        "queries/v1/006e__proportional-90-percent.sql"
    )
    if not plan_only:
        cursor.execute(pptn1_script)
    all_queries.append(pptn1_script)

    pptn2_script = load_sql_file(
        "queries/v1/006f__proportional-95-percent.sql"
    )
    if not plan_only:
        cursor.execute(pptn2_script)
    all_queries.append(pptn2_script)

    pptn3_script = load_sql_file(
        "queries/v1/006g__proportional-97-percent.sql"
    )
    if not plan_only:
        cursor.execute(pptn3_script)
    all_queries.append(pptn3_script)

    end = time.time()

    return end - start, all_queries


def run_comparison(state_abbr, cursor, district_type="old", plan_only=False):
    all_queries = []

    start = time.time()

    comparison_script = load_sql_file("queries/v1/007__compared-margins.sql")

    district_num_column = (
        DISTRICT_NUMBER_COLUMNS["old_districts"]
        if district_type == "old"
        else DISTRICT_NUMBER_COLUMNS["new_districts"]
    )
    comparison_script = comparison_script.replace(
        "{{{ district_num_column }}}", district_num_column
    )

    district_shape_table = (
        BASE_TABLE_NAMES["old_districts"]
        if district_type == "old"
        else BASE_TABLE_NAMES["new_districts"]
    )
    comparison_script = comparison_script.replace(
        "{{{ district_shape_table }}}", district_shape_table
    )

    district_id_column = (
        DISTRICT_ID_COLUMNS["old_districts"]
        if district_type == "old"
        else DISTRICT_ID_COLUMNS["new_districts"]
    )
    comparison_script = comparison_script.replace(
        "{{{ district_id_column }}}", district_id_column
    )

    if not plan_only:
        cursor.execute(comparison_script)
    all_queries.append(comparison_script)

    end = time.time()

    return end - start, all_queries


def run_full_political_analysis(
    state_raw, district_type="old", plan_only=False
):
    print("⚡ 000: Prep work")
    (prep_time, prep_queries) = run_prep(
        state_raw, district_type, plan_only=plan_only
    )
    print(f"    √ Completed in {prep_time}s.")

    state_obj, db, cursor = load_state_with_db(state_raw)

    if not state_obj:
        return -1, {}, {}

    state_abbr = state_obj.abbr.lower()

    print("⚡ 001: Divide and conquer")
    (divide_time, divide_queries) = run_division(
        state_abbr, district_type, plan_only=plan_only
    )
    print(f"    √ Completed in {divide_time}s.")

    print("⚡ 002: Re-join divisions")
    (merge_time, merge_queries) = run_merge(state_abbr, plan_only=plan_only)
    print(f"    √ Completed in {merge_time}s.")

    print("⚡ 003: Join with results")
    (join_time, join_queries) = run_join(
        state_abbr, cursor, plan_only=plan_only
    )
    print(f"    √ Completed in {join_time}s.")

    print("⚡ 004: Threshold calculations")
    (calculation_time, calculation_queries) = run_calculation(
        state_abbr, cursor, plan_only=plan_only
    )
    print(f"    √ Completed in {calculation_time}s.")

    print("⚡ 005: Precinct assembly")
    (assembly_time, assembly_queries) = run_assembly(
        state_abbr, cursor, plan_only=plan_only
    )
    print(f"    √ Completed in {assembly_time}s.")

    print("⚡ 006: Final formatting")
    (formatting_time, formatting_queries) = run_formatting(
        state_abbr, cursor, plan_only=plan_only
    )
    print(f"    √ Completed in {formatting_time}s.")

    print("⚡ 007: Comparisons")
    (comparison_time, comparison_queries) = run_comparison(
        state_abbr, cursor, district_type, plan_only=plan_only
    )
    print(f"    √ Completed in {comparison_time}s.")

    return (
        sum(
            [
                prep_time,
                divide_time,
                merge_time,
                join_time,
                calculation_time,
                assembly_time,
                formatting_time,
                comparison_time,
            ]
        ),
        dict(
            prep=prep_time,
            divide=divide_time,
            merge=merge_time,
            join=join_time,
            calculate=calculation_time,
            assembly=assembly_time,
            formatting=formatting_time,
            comparison=comparison_time,
        ),
        dict(
            prep=prep_queries,
            divide=divide_queries,
            merge=merge_queries,
            join=join_queries,
            calculate=calculation_queries,
            assembly=assembly_queries,
            formatting=formatting_queries,
            comparison=comparison_queries,
        ),
    )
