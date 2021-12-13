# Imports from PROWESS.
from config.counties.by_state.ca import CA_COUNTY_MAP
from config.counties.by_state.ia import IA_COUNTY_MAP
from config.counties.by_state.md import MD_COUNTY_MAP
from config.counties.by_state.me import ME_COUNTY_MAP
from config.counties.by_state.ore import OR_COUNTY_MAP


COUNTIES_TO_FIPS_BY_STATE = {
    "ca": CA_COUNTY_MAP,
    "ia": IA_COUNTY_MAP,
    "md": MD_COUNTY_MAP,
    "me": ME_COUNTY_MAP,
    "or": OR_COUNTY_MAP,
}
