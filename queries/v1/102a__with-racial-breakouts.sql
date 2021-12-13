SELECT
				o.dist_geoid as district_id,
				o.tract_id,
				o.coverage,
				c.total_pop AS total_pop,
				c.total_moe AS total_moe,
				c.nonwhite_pop AS nonwhite_pop,
				c.whiteonly_moe AS whiteonly_moe
    INTO "102a__with_racial_breakdowns"
    FROM "101__tract_coverages" o
    		INNER JOIN "000e__tract_racial_counts" c
            ON o.tract_id = c.split_geoid
    ORDER BY coverage;
