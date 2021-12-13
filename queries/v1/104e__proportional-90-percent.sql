WITH all_ninety_percent_rows AS (
		SELECT
						m.district_id,
						m.tract_id,
						m.coverage,
						m.raw_total_pop AS final_total_pop,
						m.raw_nonwhite_pop AS final_nonwhite_pop,
						m.raw_over_25_pop AS final_over_25_pop,
						m.raw_ba_over_25_pop AS final_ba_over_25_pop
				FROM "103a__majorities_only" m
				WHERE m.coverage >= 0.9
		UNION
				SELECT
								o.district_id,
								o.tract_id,
								o.coverage,
								o.raw_total_pop AS final_total_pop,
								o.raw_nonwhite_pop AS final_nonwhite_pop,
								o.raw_over_25_pop AS final_over_25_pop,
								o.raw_ba_over_25_pop AS final_ba_over_25_pop
						FROM "103d__grouped_with_threshold" o
						WHERE total_minority_coverage_proportion >= 0.1
		UNION
				SELECT
								n.district_id,
								n.tract_id,
								n.coverage,
								n.raw_total_pop AS final_total_pop,
								n.raw_nonwhite_pop AS final_nonwhite_pop,
								n.raw_over_25_pop AS final_over_25_pop,
								n.raw_ba_over_25_pop AS final_ba_over_25_pop
						FROM "103e__main_count_90_percent" n
)
SELECT *
		INTO "104e__proportional_90_percent"
		FROM all_ninety_percent_rows;
