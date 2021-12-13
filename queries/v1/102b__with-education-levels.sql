SELECT
				b.district_id,
				b.tract_id,
				b.coverage,
				b.total_pop,
				b.total_moe,
				b.nonwhite_pop,
				b.whiteonly_moe,
				e.over_25_pop,
				e.over_25_moe,
				e.ba_over_25_pop,
				e.ba_over_25_moe
    INTO "102b__with_educational_breakdowns"
    FROM "102a__with_racial_breakdowns" b
    		INNER JOIN "000f__tract_educational_counts" e
            ON b.tract_id = e.split_geoid
    ORDER BY b.coverage;
