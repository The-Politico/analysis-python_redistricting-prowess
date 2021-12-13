SELECT
				district_id,
				tract_id,
				coverage,
				raw_total_pop AS final_total_pop,
				raw_nonwhite_pop AS final_nonwhite_pop,
				raw_over_25_pop AS final_over_25_pop,
				raw_ba_over_25_pop AS final_ba_over_25_pop
    INTO "104d__threshold_97_percent"
    FROM "103a__majorities_only"
		WHERE coverage > 0.97;
