# Imports from other dependencies.
import geopandas as gpd
import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from sqlalchemy_utils import create_database
from sqlalchemy_utils import database_exists
import us


# Imports from PROWESS.
from config import ALPHA_STRING
from config import BASE_TABLE_NAMES
from config import DATABASE_PREFIX
from config import DISTRICT_ID_COLUMNS
from config import DISTRICT_NUMBER_COLUMNS
from config.counties import COUNTIES_TO_FIPS_BY_STATE
from config.db_configs import DB_CONFIGS
from config.divisions import DIVISIONS_FOR_STATE
from config.precinct_data import COUNTIES_AS_FIPS
from config.precinct_data import COUNTIES_AS_NAMES
from config.precinct_data import PRECINCT_CONFIGS
from utils.db import load_state_with_db
from utils.sql_io import load_sql_file


def format_county_list(counties_raw):
    counties_list = ", ".join(
        [f"'{county_code}'" for county_code in counties_raw]
    )

    return f"( {counties_list} )"


def prepare_data(
    state_raw, district_type="old", db_shard="main_archive", plan_only=False
):
    state_obj = us.states.lookup(state_raw)

    if not state_obj:
        print(f"ERROR: State not found for query '{state_raw}'.")
        return None, None, None

    state_abbr = state_obj.abbr.lower()
    state_fips = state_obj.fips

    precinct_config = PRECINCT_CONFIGS.get(state_abbr, None)

    if not precinct_config:
        print(f"ERROR: Precinct config not found for state '{state_abbr}'.")
        return None, None, None

    full_database_name = f"{DATABASE_PREFIX}__{state_abbr}"

    engine = create_engine(f"{DB_CONFIGS[db_shard]}/{full_database_name}")

    if not database_exists(engine.url):
        create_database(engine.url)
        print(f"Created database '{full_database_name}'.")
    else:
        print(f"Database '{full_database_name}' already exists.")

    extensions = [
        dict(name="postgis", tester="PostGIS_version()"),
        # dict(name="postgis_topology", tester=""),
    ]

    with engine.connect() as con:
        for extension_dict in extensions:
            try:
                results = con.execute(f"SELECT {extension_dict['tester']};")

                ext_version = "unknown"

                for result in results:
                    for row in result:
                        ext_version = row.split()[0]

                print(
                    "".join(
                        [
                            "  * Extension '",
                            extension_dict["name"],
                            f"' already present (version {ext_version}).",
                        ]
                    )
                )
            except ProgrammingError:
                extension_name = extension_dict["name"]
                con.execute(f"CREATE EXTENSION {extension_name};")

                print(f"  * Created extension '{extension_name}'.")

        #
        # CREATE EXTENSION ;

    precinct_data = gpd.read_file(
        f"raw_data/precincts_2020/{state_fips}/2020.shp"
    )

    all_final_fields = []

    precinct_data["PROWESS_county"] = (
        precinct_data[precinct_config["county_field"]]
        if precinct_config.get("county_type", COUNTIES_AS_NAMES)
        == COUNTIES_AS_FIPS
        else precinct_data[precinct_config["county_field"]]
        .map(COUNTIES_TO_FIPS_BY_STATE[state_abbr])
        .fillna(precinct_data[precinct_config["county_field"]])
    )
    all_final_fields.append("PROWESS_county")

    precinct_data["PROWESS_geoid"] = precinct_data[
        precinct_config["geoid_field"]
    ]
    all_final_fields.append("PROWESS_geoid")

    if precinct_config.get("prepend_county_to_geoid", False):
        precinct_data["PROWESS_geoid"] = (
            precinct_data["PROWESS_county"].astype(str)
            + "__"
            + precinct_data["PROWESS_geoid"]
        )

    candidates_for_state = precinct_config.get("candidate_map", {})

    if not candidates_for_state:
        print(f"ERROR: Candidate dict found in '{state_raw}' config.")
        return None, None, None
    elif "biden" not in candidates_for_state:
        print(f"ERROR: Biden votes not found in '{state_raw}' precincts.")
        return None, None, None
    elif "trump" not in candidates_for_state:
        print(f"ERROR: Trump votes not found in '{state_raw}' precincts.")
        return None, None, None

    precinct_data["PROWESS_biden_raw"] = precinct_data[
        candidates_for_state["biden"]
    ]
    all_final_fields.append("PROWESS_biden_raw")

    precinct_data["PROWESS_trump_raw"] = precinct_data[
        candidates_for_state["trump"]
    ]
    all_final_fields.append("PROWESS_trump_raw")

    precinct_data["PROWESS_all_potus_raw"] = precinct_data[
        precinct_config["candidate_map"].values()
    ].sum(axis=1)
    all_final_fields.append("PROWESS_all_potus_raw")

    all_extra_fields = precinct_config.get("extra_fields", {})

    if all_extra_fields:
        for original_name, formatted_name in all_extra_fields.items():
            new_field_name = f"PROWESS_{formatted_name}"
            precinct_data[new_field_name] = precinct_data[original_name]
            all_final_fields.append(new_field_name)

    # Convert shapefile to universal-use CRS.
    precinct_data = precinct_data.to_crs("EPSG:4326")

    # Filter to only final fields.
    # precinct_data = precinct_data[all_final_fields]
    final_precinct_data = gpd.GeoDataFrame.from_features(
        precinct_data,
        crs=precinct_data.crs,
        columns=[*all_final_fields, "geometry"],
    )

    # Remove the PROWESS prefix from final fields.
    final_precinct_data = final_precinct_data.rename(
        columns={
            field: field.replace("PROWESS_", "") for field in all_final_fields
        }
    )

    district_data = None

    if district_type == "old":
        nationwide_old_districts = gpd.read_file(
            f"raw_data/old_districts/{state_fips}/circa2018.shp"
        )
        nationwide_old_districts = nationwide_old_districts.to_crs("EPSG:4326")

        district_data = nationwide_old_districts[
            (nationwide_old_districts["STATEFP"] == state_fips)
            & ~(nationwide_old_districts["CD116FP"].isin(["98", "ZZ"]))
        ]
    elif district_type == "new":
        new_dist_path = f"raw_data/new_districts/{state_fips}/toEvaluate.shp"

        if os.path.isfile(new_dist_path):
            district_data = gpd.read_file(new_dist_path)

            district_data = district_data.to_crs("EPSG:4326")

    if district_data is None:
        print(f"ERROR: New districts not found for '{state_raw}'.")
        return None, None, None

    district_shape_table = (
        BASE_TABLE_NAMES["old_districts"]
        if district_type == "old"
        else BASE_TABLE_NAMES["new_districts"]
    )

    if not plan_only:
        final_precinct_data.to_postgis("000a__precincts", engine)

        district_data.to_postgis(district_shape_table, engine)

    return precinct_data, district_data, engine


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
