COUNTIES_AS_FIPS = "asFips"
COUNTIES_AS_NAMES = "asNames"

PRECINCT_CONFIGS = {
    "al": dict(
        county_field="COUNTYFP20",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="GEOID20",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            write_ins="G20PREOWRI",  # others
        ),
    ),
    "ak": dict(
        county_field="COUNTYFP20",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="DISTRICT",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            janos="G20PREGJAN",  # green party
            blankenship="G20PRECBLA",  # conservative party
            pierce="G20PREIPIE",  # independent
            de_la_fuente="G20PREOFUE",  # alliance party
        ),
    ),
    "ar": dict(
        county_field="COUNTY_FIP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="PRECINCT",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            blankenship="G20PRECBLA",  # constitution party
            carroll="G20PREACAR",  # american solidarity party
            myers="G20PREOMYE",  # life and liberty party
            la_riva="G20PRESLAR",  # socialism and liberation party
            west="G20PREIWES",  # independent
            collins="G20PREICOL",  # independent
            pierce="G20PREIPIE",  # independent
            gammon="G20PREIGAM",  # independent
            de_la_fuente="G20PREIFUE",  # independent
        ),
    ),
    "az": dict(
        county_field="CDE_COUNTY",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="PCTNUM",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
        ),
    ),
    "ca": dict(
        county_field="COUNTY",
        county_type=COUNTIES_AS_NAMES,
        geoid_field="SRPREC_KEY",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            de_la_fuente_guerra="G20PREAFUE",  # american independent party
            la_riva="G20PREPLAR",  # peace and freedom party
        ),
    ),
    "co": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="VTDST",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            blankenship="G20PRECBLA",  # american constitution party
            west="G20PREUWES",  # unaffiliated
            others="G20PREOOTH",  # etc
        ),
    ),
    "ct": dict(
        county_field="COUNTYFP20",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="NAME20",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            write_ins="G20PREOWRI",  # others
        ),
    ),
    "de": dict(
        county_field="COUNTYFP20",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="PRECINCT",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party of delaware
        ),
    ),
    "fl": dict(
        county_field="county",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="pct_std",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            de_la_fuente="G20PREODEL",  # reform party
            la_riva="G20PRESLAR",  # party for socialism and liberation
            hawkin="G20PREGHAW",  # green party
            blankenship="G20PRECBLA",  # constitution party
            write_ins="G20PREOWRI",  # others
        ),
    ),
    "ga": dict(
        county_field="CTYNUMBER2",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="DISTRICT",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            trump="C20PRERTRU",  # republican party
            biden="C20PREDBID",  # democratic party
            jorgensen="C20PRELJOR",  # libertarian party
        ),
    ),
    "hi": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="GEOID",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            blankenship="G20PRECBLA",  # conservative party
            pierce="G20PREOPIE",  # american shopping party
        ),
    ),
    "ia": dict(
        county_field="COUNTY",
        county_type=COUNTIES_AS_NAMES,
        geoid_field="DISTRICT",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            blakenship="G20PRECBLA",  # constitution party
            de_la_fuente="G20PREOFUE",  # alliance party
            king="G20PREOKIN",  # genealogy know your family history party
            west="G20PREIWES",  # independent
            pierce="G20PREIPIE",  # independent
            write_ins="G20PREOWRI",  # others
        ),
    ),
    "id": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="VTDST",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            west="G20PREIWES",  # independent
            pierce="G20PREIPIE",  # independent
            blankenship="G20PREIBLA",  # constitution party
            de_la_fuente="G20PREIFUE",  # independent
        ),
    ),
    "il": dict(
        county_field="COUNTYFP20",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="GEOID20",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            carroll="G20PREACAR",  # american solidarity party
            la_riva="G20PRESLAR",  # party for socialism and liberation
        ),
    ),
    "in": dict(
        county_field="COUNTYFP20",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="GEOID20",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
        ),
    ),
    "ks": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="VTDST",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
        ),
    ),
    "ky": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="GEOID",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            west="G20PREOWES",  # the birthday party
            others="G20PREOOTH",  # other candidates
        ),
    ),
    "la": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="VTDST",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            west="G20PREOWES",  # the birthday party
            others="G20PREOOTH",  # other candidates
        ),
    ),
    "ma": dict(
        county_field="TOWN_ID",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="WP_NAME",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic-farmer-labor party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            write_ins="G20PREOWRI",  # others
        ),
    ),
    "md": dict(
        county_field="JURSCODE",
        county_type=COUNTIES_AS_NAMES,
        geoid_field="NAME",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            segal="G20PREBSEG",  # bread and roses party
            write_ins="G20PREOWRI",  # others
        ),
    ),
    "me": dict(
        county_field="COUNTY20",
        county_type=COUNTIES_AS_NAMES,
        geoid_field="NAME20",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green independent party
            de_la_fuente="G20PREAFUE",  # alliance party
        ),
    ),
    "mi": dict(
        county_field="COUNTYFIPS",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="PRECINCTID",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            de_la_fuente="G20PRENDEL",  # natural law party
            blankenship="G20PRETBLA",  # us taxpayers party
        ),
    ),
    "mn": dict(
        county_field="COUNTYFIPS",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="VTDID",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic-farmer-labor party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            de_la_fuente="G20PREAFUE",  # independence-alliance party
            la_riva="G20PREPLAR",  # socialism and liberation party
            kennedy="G20PRESKEN",  # socialist workers party
            west="G20PREIWES",  # independent
            pierce="G20PREIPIE",  # independent
            write_ins="G20PREOWRI",  # others
        ),
    ),
    "mo": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="NAME",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            blankenship="G20PRECBLA",  # constitution party
        ),
    ),
    "ms": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="GEOID",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            other_candidates="G20PREOOTH",  # other candidates on ballot
        ),
    ),
    "mt": dict(
        county_field="COUNTYFP10",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="SOSPRECINC",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
        ),
    ),
    "nc": dict(
        county_field="COUNTY_ID",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="PREC_ID",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            blankenship="G20PRECBLA",  # constitution party
            write_ins="G20PREOWRI",  # others
        ),
    ),
    "nd": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="PRECINCT",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            write_ins="G20PREOWRI",  # others
        ),
    ),
    "ne": dict(
        county_field="COUNTY",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="NAME",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
        ),
    ),
    "nm": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="GEOID",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            other_candidates="G20PREOOTH",  # other candidates on ballot
        ),
    ),
    "nh": dict(
        county_field="COUNTYFP20",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="GEOID20",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
        ),
    ),
    "nj": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="GEOID",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            other_candidates="G20PREOOTH",  # other candidates on ballot
        ),
    ),
    "nv": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="VTDST",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
            blankenship="G20PREIBLA",  # independent american party
            none_of_these="G20PREONON",  # "none of these candidates"
        ),
    ),
    "ny": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="PRECINCT",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic and working families fusion
            trump="G20PRERTRU",  # republican and conservative fusion
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # pacific green party
            pierce="G20PREIPIE",  # independence party
            write_ins="G20PREOWRI",  # others
        ),
    ),
    "oh": dict(
        county_field="COUNTYFP20",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="GEOID20",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # independent
        ),
    ),
    "ok": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="GEOID",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            west="G20PREIWES",  # independent
            simmons="G20PREISIM",  # independent
            pierce="G20PREIPIE",  # independent
        ),
    ),
    "or": dict(
        county_field="COUNTY",
        county_type=COUNTIES_AS_NAMES,
        geoid_field="NAME",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # pacific green party
            hunter="G20PREPHUN",  # progressive party
            write_ins="G20PREOWRI",  # others
        ),
    ),
    "pa": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="GEOID",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            other_candidates="G20PREOOTH",  # other candidates on ballot
        ),
    ),
    "ri": dict(
        county_field="COUNTYFP20",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="GEOID20",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
            de_la_fuente="G20PREOFUE",  # alliance party
            la_rive="G20PREOLAR",  # socialism and liberation party
            carroll="G20PREOCAR",  # american solidarity party
            write_ins="G20PREOWRI",  # others
        ),
    ),
    "sc": dict(
        county_field="COUNTY",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="PCODE",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            de_la_fuente="G20PREAFUE",  # alliance party
        ),
    ),
    "sd": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="GEOID",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            other_candidates="G20PREOOTH",  # other candidates on ballot
        ),
    ),
    "tn": dict(
        county_field="COUNTY",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="NAME",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # Republican Party
            biden="G20PREDBID",  # Democratic Party
            jorgensen="G20PRELJOR",  # Libertarian Party
            hawkins="G20PREGHAW",  # Green Party
            west="G20PREIWES",  # Independent
            blankenship="G20PREIBLA",  # Independent
            kennedy="G20PREIKEN",  # Independent
            la_riva="G20PREILAR",  # Independent
            de_la_fuente="G20PREIFUE",  # Independent
        ),
    ),
    "tx": dict(
        county_field="CNTY",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="PCTKEY",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            write_ins="G20PREOWRI",  # others
        ),
        # extra_fields={
        #     "G20VR": "raw_voters",
        #     "G20SSVR": "raw_spanish_surname_voters",
        # },
    ),
    "ut": dict(
        county_field="CountyID",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="resultspre",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            blankenship="G20PRECBLA",  # constitution party
            pierce="G20PREIPIE",  # unaffiliated
            west="G20PREIWES",  # unaffiliated
            mchugh="G20PREIMCH",  # unaffiliated
            la_riva="G20PREILAR",  # unaffiliated
            write_ins="G20PREOWRI",  # others
        ),
    ),
    "vt": dict(
        county_field="COUNTYFP20",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="NAME20",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            west="G20PREIWES",  # independent
            other_candidates="G20PREOOTH",  # other candidates on ballot
            sanders="G20PREOSAN",  # write-in
            other_write_ins="G20PREOWRI",  # others candidates
        ),
    ),
    "va": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="VTDST",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
            write_ins="G20PREOWRI",  # others
        ),
    ),
    "wa": dict(
        county_field="COUNTY",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="ST_CODE",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
            hawkins="G20PREGHAW",  # green party
            la_riva="G20PRESLAR",  # socialism and liberation party
            kennedy="G20PRESKEN",  # socialist workers party
            write_ins="G20PREOWRI",  # others
        ),
    ),
    "wi": dict(
        county_field="CNTY_FIPS",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="GEOID",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            jorgensen="G20PRELJOR",  # libertarian party
            blankenship="G20PRECBLA",  # constitution party
            carroll="G20PREICAR",  # independent
            hawkins="G20PREOHAW",  # independent write-in
            west="G20PREOWES",  # independent write-in
            la_riva="G20PREOLAR",  # independent write-in
            charles="G20PREOCHA",  # independent write-in
            simmons="G20PREOSIM",  # independent write-in
            wells="G20PREOWEL",  # independent write-in
            boddie="G20PREOBOD",  # independent write-in
            write_ins="G20PREOWRI",  # other write-in votes
        ),
    ),
    "wv": dict(
        county_field="COUNTYFP",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="GEOID",
        prepend_county_to_geoid=False,
        geometry_field="geometry",
        candidate_map=dict(
            biden="G20PREDBID",  # democratic party
            trump="G20PRERTRU",  # republican party
            other_candidates="G20PREOOTH",  # other candidates on ballot
        ),
    ),
    "wy": dict(
        county_field="COUNTYFP20",
        county_type=COUNTIES_AS_FIPS,
        geoid_field="VTDST20",
        prepend_county_to_geoid=True,
        geometry_field="geometry",
        candidate_map=dict(
            trump="G20PRERTRU",  # republican party
            biden="G20PREDBID",  # democratic party
            jorgensen="G20PRELJOR",  # libertarian party
            pierce="G20PREIPIE",  # independent
            write_ins="G20PREOWRI",  # others
        ),
    ),
}
