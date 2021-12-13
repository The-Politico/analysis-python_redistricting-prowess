# Imports from other dependencies.
import psycopg2
import us


# Imports from PROWESS.
from config import DATABASE_PREFIX
from config.db_configs import DB_CONFIGS


def load_state_with_db(state_raw, db_shard="main_archive", db_suffix=None):
    state_obj = us.states.lookup(state_raw)

    if not state_obj:
        print(f"ERROR: State not found for query '{state_raw}'.")
        return None, None, None

    state_abbr = state_obj.abbr.lower()

    full_database_name = (
        f"{DATABASE_PREFIX}__{state_abbr}"
        if not db_suffix
        else f"{DATABASE_PREFIX}__{state_abbr}__{db_suffix}"
    )

    shard_db = psycopg2.connect(f"{DB_CONFIGS[db_shard]}/{full_database_name}")

    shard_db.autocommit = True

    shard_cursor = shard_db.cursor()

    return state_obj, shard_db, shard_cursor
