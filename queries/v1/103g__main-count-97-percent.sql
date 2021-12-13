SELECT
				m.district_id,
				m.tract_id,
				m.coverage,
				(m.raw_total_pop - g.minority_total_pop_portion) AS raw_total_pop,
				(m.raw_nonwhite_pop - g.minority_nonwhite_pop_portion) AS raw_nonwhite_pop,
				(m.raw_over_25_pop - g.minority_over_25_pop_portion) AS raw_over_25_pop,
				(m.raw_ba_over_25_pop - g.minority_ba_over_25_pop_portion) AS raw_ba_over_25_pop
    INTO "103g__main_count_97_percent"
    FROM "103a__majorities_only" m
		    INNER JOIN "103c__grouped_minorities" g
				    ON m.tract_id = g.tract_id
		WHERE coverage < 0.97;
