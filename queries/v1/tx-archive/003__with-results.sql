SELECT
				o.dist_geoid as district_id,
				o.precinct_id,
				o.coverage,
				p.trump_raw AS raw_trump_votes,
				p.biden_raw AS raw_biden_votes,
				p.all_potus_raw AS raw_all_potus_votes
				-- p."G20VR" AS raw_voters,
        -- p."G20SSVR" AS raw_spanish_surname_voters
    INTO "003__with_results"
    FROM "002__concatenated" o
    		INNER JOIN "000a__precincts" p
            ON o.precinct_id = p.geoid
    ORDER BY coverage;
