SELECT
				district_id,
				precinct_id,
				coverage,
				FLOOR(raw_trump_votes * coverage) AS raw_trump_votes,
				FLOOR(raw_biden_votes * coverage) AS raw_biden_votes,
				FLOOR(raw_all_potus_votes * coverage) AS raw_all_potus_votes
				-- FLOOR(raw_voters * coverage) AS raw_voters,
				-- (raw_spanish_surname_voters * coverage) AS raw_spanish_surname_voters
    INTO "004b__significant_minorities"
    FROM "003__with_results"
    WHERE coverage > 0.01
		    AND coverage < 0.5;
