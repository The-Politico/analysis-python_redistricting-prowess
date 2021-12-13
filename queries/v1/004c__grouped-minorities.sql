SELECT
				precinct_id,
				SUM(raw_trump_votes) AS minority_trump_portion,
				SUM(raw_biden_votes) AS minority_biden_portion,
				SUM(raw_all_potus_votes) AS minority_all_potus_portion,
        SUM(coverage) AS total_minority_coverage_proportion,
				COUNT(district_id) AS minority_portions
    INTO "004c__grouped_minorities"
    FROM "004b__significant_minorities"
		GROUP BY precinct_id;
