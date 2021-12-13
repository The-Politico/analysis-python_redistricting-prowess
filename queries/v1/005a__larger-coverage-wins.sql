SELECT
				district_id,
				precinct_id,
				coverage,
				raw_trump_votes AS final_trump_votes,
				raw_biden_votes AS final_biden_votes,
				raw_all_potus_votes AS final_all_potus_votes
    INTO "005a__larger_coverage_wins"
    FROM "004a__majorities_only";
