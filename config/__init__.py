ALPHA_STRING = "abcdefghijklmnopqrstuvwxyz"

BASE_TABLE_NAMES = dict(
    old_districts="000b__old_districts",
    new_districts="000c__new_districts",
    tract_geogs="000d__tract_geographies",
    tract_racial_counts="000e__tract_racial_counts",
    tract_edu_counts="000f__tract_educational_counts",
)

# DISTRICT_ID_COLUMNS = dict(old_districts="GEOID", new_districts="geoid")
DISTRICT_ID_COLUMNS = dict(old_districts="geoid", new_districts="geoid")

DISTRICT_NUMBER_COLUMNS = dict(
    # old_districts="CD116FP",
    old_districts="dist_num",
    new_districts="dist_num",
)

# DATABASE_PREFIX = "prowess_v1_old"
DATABASE_PREFIX = "prowess_v1_new"
