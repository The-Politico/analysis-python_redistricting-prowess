WITH preliminary_output AS (
		SELECT
						district_id,
						SUM(final_total_pop) AS total_pop,
						SUM(final_nonwhite_pop) AS nonwhite_pop,
						SUM(final_over_25_pop) AS over_25_pop,
						SUM(final_ba_over_25_pop) AS ba_over_25_pop
				FROM "104b__threshold_90_percent"
				GROUP BY district_id
)
SELECT
				district_id,
				(
						(nonwhite_pop / total_pop) * 100
				) AS nonwhite_pct,
				nonwhite_pop,
				total_pop,
				(
						(ba_over_25_pop / over_25_pop) * 100
				) AS bachelors_pct,
				ba_over_25_pop,
				over_25_pop
		INTO "105b__threshold_90_percent"
		FROM preliminary_output
		WHERE total_pop > 0
		ORDER BY nonwhite_pct DESC;
