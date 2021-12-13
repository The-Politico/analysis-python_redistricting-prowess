SELECT
				o.dist_geoid as district_id,
				o.precinct_id,
				o.coverage,
				p.trump_raw AS raw_trump_votes,
				p.biden_raw AS raw_biden_votes,
				p.all_potus_raw AS raw_all_potus_votes
    INTO "003__with_results"
    FROM "002__concatenated" o
    		INNER JOIN "000a__precincts" p
            ON o.precinct_id = p.geoid
    ORDER BY coverage;
