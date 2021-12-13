# Imports from other dependencies.
import psycopg2
import us


# Imports from PROWESS.
from config import ALPHA_STRING
from config import DATABASE_PREFIX
from config.db_configs import DB_CONFIGS
from config.divisions import DIVISIONS_FOR_STATE
from utils.sql_io import load_sql_file


def merge_divisions(state_raw, db_shard="main_archive", plan_only=False):
    state_obj = us.states.lookup(state_raw)

    if not state_obj:
        print(f"ERROR: State not found for query '{state_raw}'.")
        return None, None, None

    state_abbr = state_obj.abbr.lower()
    # state_fips = state_obj.fips

    full_database_name = f"{DATABASE_PREFIX}__{state_abbr}"

    shard_db = psycopg2.connect(f"{DB_CONFIGS[db_shard]}/{full_database_name}")

    shard_db.autocommit = True

    shard_cursor = shard_db.cursor()

    all_divisions_list = list(DIVISIONS_FOR_STATE.get(state_abbr, ()))

    if not all_divisions_list:
        print("ERROR: No divisions.")
        return None

    all_division_scripts = {}

    # First, process the first division we see.
    print(f"Merging division '{all_divisions_list[0]}'...")

    initial_division_script = load_sql_file(
        "queries/v1/002a__rejoin-initial.sql"
    )

    initial_division_table = "__".join(
        [f"001{ALPHA_STRING[0]}", f"divided_precincts_{all_divisions_list[0]}"]
    )

    initial_division_script = initial_division_script.replace(
        "{{{ division_table }}}", initial_division_table
    )

    if not plan_only:
        shard_cursor.execute(initial_division_script)

    all_division_scripts[all_divisions_list[0]] = initial_division_script

    print("    Division done!")

    # Now process all other divisions.
    subsequent_division_template = load_sql_file(
        "queries/v1/002b__rejoin-subsequent.sql"
    )

    for counter, division_slug in enumerate(all_divisions_list[1:]):
        print(f"Merging division '{division_slug}'...")

        subsequent_division_script = f"{subsequent_division_template}"

        subsequent_division_table = "__".join(
            [
                f"001{ALPHA_STRING[counter + 1]}",
                f"divided_precincts_{division_slug}",
            ]
        )

        subsequent_division_script = subsequent_division_script.replace(
            "{{{ division_table }}}", subsequent_division_table
        )

        if not plan_only:
            shard_cursor.execute(subsequent_division_script)

        all_division_scripts[division_slug] = subsequent_division_script

        print("    Division done!")

    return all_division_scripts
