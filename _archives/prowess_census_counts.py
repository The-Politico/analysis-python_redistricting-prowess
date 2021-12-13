# Imports from other dependencies.
import geopandas as gpd
import os
import pandas as pd


# import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from sqlalchemy_utils import create_database
from sqlalchemy_utils import database_exists
import us


# Imports from PROWESS.
from config import BASE_TABLE_NAMES
from config import DATABASE_PREFIX
from config.db_configs import DB_CONFIGS
from config import DISTRICT_ID_COLUMNS
from config import DISTRICT_NUMBER_COLUMNS
from utils.db import load_state_with_db
from utils.pandas_to_psql import upload_df_to_psql
from utils.sql_io import load_sql_file


def prepare_tract_data(
    state_raw, district_type="old", db_shard="main_archive", plan_only=False
):
    state_obj = us.states.lookup(state_raw)

    if not state_obj:
        print(f"ERROR: State not found for query '{state_raw}'.")
        return None, None, None, None

    state_abbr = state_obj.abbr.lower()
    state_fips = state_obj.fips

    full_database_name = f"{DATABASE_PREFIX}__{state_abbr}__census"

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

    tract_geographies = gpd.read_file(
        f"raw_data/census_tract_geographies/{state_fips}/tracts2019.shp"
    )

    # Convert shapefile to universal-use CRS.
    tract_geographies = tract_geographies.to_crs("EPSG:4326")

    # Filter to only final fields.
    final_tract_geographies = gpd.GeoDataFrame.from_features(
        tract_geographies,
        crs=tract_geographies.crs,
        columns=["STATEFP", "COUNTYFP", "TRACTCE", "GEOID", "geometry"],
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
        return None, None, None, None

    district_shape_table = (
        BASE_TABLE_NAMES["old_districts"]
        if district_type == "old"
        else BASE_TABLE_NAMES["new_districts"]
    )

    education_level_df = pd.read_csv(
        f"raw_data/census_education_level/{state_fips}/auto_gen.csv",
        header=[0],
    )

    education_level_cols_formatted = dict(
        GEO_ID="geoid",
        S1501_C01_006E="over_25_pop",
        S1501_C01_006M="over_25_moe",
        S1501_C01_015E="ba_over_25_pop",
        S1501_C01_015M="ba_over_25_moe",
    )

    education_level_df = education_level_df.rename(
        columns=education_level_cols_formatted
    )

    education_level_df = education_level_df[
        education_level_cols_formatted.values()
    ]

    education_level_df["split_geoid"] = education_level_df[
        "geoid"
    ].str.replace("1400000US", "")

    racial_count_df = pd.read_csv(
        f"raw_data/census_race_plus_hl/{state_fips}/auto_gen.csv",
        header=[0],
    )

    racial_count_cols_formatted = dict(
        GEO_ID="geoid",
        B03002_001E="total_pop",
        B03002_001M="total_moe",
        B03002_003E="whiteonly_pop",
        B03002_003M="whiteonly_moe",
    )

    racial_count_df = racial_count_df.rename(
        columns=racial_count_cols_formatted
    )

    racial_count_df = racial_count_df[racial_count_cols_formatted.values()]

    racial_count_df["split_geoid"] = racial_count_df["geoid"].str.replace(
        "1400000US", ""
    )

    racial_count_df["nonwhite_pop"] = (
        racial_count_df["total_pop"] - racial_count_df["whiteonly_pop"]
    )

    if not plan_only:
        final_tract_geographies.to_postgis(
            BASE_TABLE_NAMES["tract_geogs"], engine
        )

        district_data.to_postgis(district_shape_table, engine)

        upload_df_to_psql(
            engine, education_level_df, BASE_TABLE_NAMES["tract_edu_counts"]
        )
        upload_df_to_psql(
            engine, racial_count_df, BASE_TABLE_NAMES["tract_racial_counts"]
        )

    return tract_geographies, district_data, racial_count_df, engine


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
