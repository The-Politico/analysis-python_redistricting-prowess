WITH all_ninety_seven_percent_rows AS (
		SELECT
						m.district_id,
						m.tract_id,
						m.coverage,
						m.raw_total_pop AS final_total_pop,
						m.raw_nonwhite_pop AS final_nonwhite_pop,
						m.raw_over_25_pop AS final_over_25_pop,
						m.raw_ba_over_25_pop AS final_ba_over_25_pop
				FROM "103a__majorities_only" m
				WHERE m.coverage >= 0.97
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
						WHERE total_minority_coverage_proportion >= 0.03
		UNION
				SELECT
								n.district_id,
								n.tract_id,
								n.coverage,
								n.raw_total_pop AS final_total_pop,
								n.raw_nonwhite_pop AS final_nonwhite_pop,
								n.raw_over_25_pop AS final_over_25_pop,
								n.raw_ba_over_25_pop AS final_ba_over_25_pop
						FROM "103g__main_count_97_percent" n
)
SELECT *
		INTO "104g__proportional_97_percent"
		FROM all_ninety_seven_percent_rows;
