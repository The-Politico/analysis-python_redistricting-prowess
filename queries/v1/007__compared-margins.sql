SELECT
  			s."{{{ district_num_column }}}" AS district,
				a.biden_pct AS biden_largestonly,
				b.biden_pct AS biden_threshold90,
				c.biden_pct AS biden_threshold95,
				d.biden_pct AS biden_threshold97,
				e.biden_pct AS biden_proportional90,
				f.biden_pct AS biden_proportional95,
				g.biden_pct AS biden_proportional97
		INTO "007__compared_margins"
		FROM "006a__larger_coverage_wins" a
        INNER JOIN "{{{ district_shape_table }}}" s
            ON a.district_id = s."{{{ district_id_column }}}"
				INNER JOIN "006b__threshold_90_percent" b
						ON a.district_id = b.district_id
				INNER JOIN "006c__threshold_95_percent" c
						ON a.district_id = c.district_id
				INNER JOIN "006d__threshold_97_percent" d
						ON a.district_id = d.district_id
				INNER JOIN "006e__proportional_90_percent" e
						ON a.district_id = e.district_id
				INNER JOIN "006f__proportional_95_percent" f
						ON a.district_id = f.district_id
				INNER JOIN "006g__proportional_97_percent" g
						ON a.district_id = g.district_id;
