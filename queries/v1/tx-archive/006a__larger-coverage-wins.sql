WITH preliminary_output AS (
		SELECT
						district_id,
						SUM(final_trump_votes) AS trump_sum,
						SUM(final_biden_votes) AS biden_sum,
						SUM(final_all_potus_votes) AS all_potus_sum
						-- SUM(final_voters) AS voters_sum,
						-- SUM(final_spanish_surname_voters) AS spanish_surname_voters_sum
				FROM "005a__larger_coverage_wins"
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
				-- voters_sum,
				-- spanish_surname_voters_sum
		INTO "006a__larger_coverage_wins"
		FROM preliminary_output
		ORDER BY biden_pct DESC;
