SELECT
				tract_id,
				SUM(raw_total_pop) AS minority_total_pop_portion,
				SUM(raw_nonwhite_pop) AS minority_nonwhite_pop_portion,
				SUM(raw_over_25_pop) AS minority_over_25_pop_portion,
				SUM(raw_ba_over_25_pop) AS minority_ba_over_25_pop_portion,
        SUM(coverage) AS total_minority_coverage_proportion,
				COUNT(district_id) AS minority_portions
    INTO "103c__grouped_minorities"
    FROM "103b__significant_minorities"
		GROUP BY tract_id;
