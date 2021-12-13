SELECT
				m.district_id,
				m.precinct_id,
				m.coverage,
				(m.raw_trump_votes - g.minority_trump_portion) AS raw_trump_votes,
				(m.raw_biden_votes - g.minority_biden_portion) AS raw_biden_votes,
				(m.raw_all_potus_votes - g.minority_all_potus_portion) AS raw_all_potus_votes
    INTO "004f__main_count_95_percent"
    FROM "004a__majorities_only" m
		    INNER JOIN "004c__grouped_minorities" g
				    ON m.precinct_id = g.precinct_id
		WHERE coverage < 0.95;
