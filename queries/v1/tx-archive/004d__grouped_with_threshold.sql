SELECT
				s.district_id,
				s.precinct_id,
				s.coverage,
				s.raw_trump_votes,
				s.raw_biden_votes,
				s.raw_all_potus_votes,
				-- s.raw_voters,
				-- s.raw_spanish_surname_voters,
				g.total_minority_coverage_proportion
    INTO "004d__grouped_with_threshold"
    FROM "004b__significant_minorities" s
		    INNER JOIN "004c__grouped_minorities" g
				    ON s.precinct_id = g.precinct_id;
