WITH all_ninety_percent_rows AS (
		SELECT
						m.district_id,
						m.precinct_id,
						m.coverage,
						m.raw_trump_votes AS final_trump_votes,
						m.raw_biden_votes AS final_biden_votes,
						m.raw_all_potus_votes AS final_all_potus_votes
						-- m.raw_voters AS final_voters,
						-- m.raw_spanish_surname_voters AS final_spanish_surname_voters
				FROM "004a__majorities_only" m
				WHERE m.coverage >= 0.9
		UNION
				SELECT
								o.district_id,
								o.precinct_id,
								o.coverage,
								o.raw_trump_votes AS final_trump_votes,
								o.raw_biden_votes AS final_biden_votes,
								o.raw_all_potus_votes AS final_all_potus_votes
								-- o.raw_voters AS final_voters,
								-- o.raw_spanish_surname_voters AS final_spanish_surname_voters
						FROM "004d__grouped_with_threshold" o
						WHERE total_minority_coverage_proportion >= 0.1
		UNION
				SELECT
								n.district_id,
								n.precinct_id,
								n.coverage,
								n.raw_trump_votes AS final_trump_votes,
								n.raw_biden_votes AS final_biden_votes,
								n.raw_all_potus_votes AS final_all_potus_votes
								-- n.raw_voters AS final_voters,
								-- n.raw_spanish_surname_voters AS final_spanish_surname_voters
						FROM "004e__main_count_90_percent" n
)
SELECT *
		INTO "005e__proportional_90_percent"
		FROM all_ninety_percent_rows;
