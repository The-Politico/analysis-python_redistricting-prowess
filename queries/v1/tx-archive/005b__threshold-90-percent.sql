SELECT
				district_id,
				precinct_id,
				coverage,
				raw_trump_votes AS final_trump_votes,
				raw_biden_votes AS final_biden_votes,
				raw_all_potus_votes AS final_all_potus_votes
				-- raw_voters AS final_voters,
				-- raw_spanish_surname_voters AS final_spanish_surname_voters
    INTO "005b__threshold_90_percent"
    FROM "004a__majorities_only"
		WHERE coverage > 0.9;
