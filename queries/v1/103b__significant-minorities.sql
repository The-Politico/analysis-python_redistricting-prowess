SELECT
				district_id,
				tract_id,
				coverage,
				FLOOR(total_pop * coverage) AS raw_total_pop,
				FLOOR(nonwhite_pop * coverage) AS raw_nonwhite_pop,
				total_moe AS overall_total_moe,
				whiteonly_moe AS overall_whiteonly_moe,
				FLOOR(over_25_pop * coverage) AS raw_over_25_pop,
				FLOOR(ba_over_25_pop * coverage) AS raw_ba_over_25_pop,
				over_25_moe AS over_25_moe,
				ba_over_25_moe AS ba_over_25_moe
    INTO "103b__significant_minorities"
    FROM "102b__with_educational_breakdowns"
    WHERE coverage > 0.05
		    AND coverage < 0.5;
