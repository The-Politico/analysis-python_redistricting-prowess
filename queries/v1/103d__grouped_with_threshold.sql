SELECT
				s.district_id,
				s.tract_id,
				s.coverage,
				s.raw_total_pop,
				s.raw_nonwhite_pop,
				s.raw_over_25_pop,
				s.raw_ba_over_25_pop,
				g.total_minority_coverage_proportion
    INTO "103d__grouped_with_threshold"
    FROM "103b__significant_minorities" s
		    INNER JOIN "103c__grouped_minorities" g
				    ON s.tract_id = g.tract_id;
