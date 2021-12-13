SELECT
        district_id,
        tract_id,
        coverage,
        total_pop AS raw_total_pop,
        total_moe AS raw_total_moe,
        nonwhite_pop AS raw_nonwhite_pop,
        whiteonly_moe AS raw_whiteonly_moe,
        over_25_pop AS raw_over_25_pop,
				over_25_moe AS raw_over_25_moe,
				ba_over_25_pop AS raw_ba_over_25_pop,
				ba_over_25_moe AS raw_ba_over_25_moe
    INTO "103a__majorities_only"
    FROM "102b__with_educational_breakdowns"
    WHERE coverage > 0.5;
