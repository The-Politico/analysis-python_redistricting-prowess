WITH preliminary_output AS (
		SELECT
						district_id,
						SUM(final_trump_votes) AS trump_sum,
						SUM(final_biden_votes) AS biden_sum,
						SUM(final_all_potus_votes) AS all_potus_sum
				FROM "005b__threshold_90_percent"
				GROUP BY district_id
)
SELECT
				district_id,
				(
						(biden_sum / (trump_sum + biden_sum)) * 100
				) AS biden_pct,
				trump_sum,
				biden_sum,
				all_potus_sum
		INTO "006b__threshold_90_percent"
		FROM preliminary_output
		WHERE trump_sum > 0
				OR biden_sum > 0
		ORDER BY biden_pct DESC;
