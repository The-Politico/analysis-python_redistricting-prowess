# Imports from python.
from pathlib import Path


# Imports from other dependencies.
import geopandas as gpd


# import psycopg2
import us


def convert_hydrography(state_raw):
    state_obj = us.states.lookup(state_raw)

    print(f"  STEP 1: Read {state_obj.name} state shapefile.")

    raw_hydro = gpd.read_file(
        "".join(
            [
                f"raw_data/hydrography/{state_obj.fips}/",
                "002__merged-counties/mergedHydro.shp",
            ]
        )
    )

    raw_hydro = raw_hydro.to_crs("EPSG:3857")

    print("  STEP 2: Dissolving features to one multipolygon.")

    gathered_hydro = raw_hydro.dissolve()

    print("  STEP 3: Splitting multipolygon into (county-spanning) features.")

    individual_features = gathered_hydro.explode(index_parts=True)

    print("  STEP 4: Calculating area.")

    total_area = sum(individual_features["geometry"].area)

    individual_features["COVER_PCT"] = (
        individual_features["geometry"].area / total_area
    ) * 100

    print("  STEP 5: Format and export grouped shapefile.")

    output_dir = f"raw_data/hydrography/{state_obj.fips}/003__grouped"
    output_file = f"{output_dir}/hydroGroup.shp"

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    individual_features = individual_features.to_crs("EPSG:4326")

    final_hydro_data = gpd.GeoDataFrame.from_features(
        individual_features,
        crs=individual_features.crs,
        columns=["COVER_PCT", "geometry"],
    )

    final_hydro_data.to_file(output_file)

    print("√ DONE.")

    return output_file
