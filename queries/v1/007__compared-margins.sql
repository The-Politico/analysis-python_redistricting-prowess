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
		FROM "{{{ district_shape_table }}}" s
        LEFT JOIN "006a__larger_coverage_wins" a
            ON s."{{{ district_id_column }}}" = a.district_id
				LEFT JOIN "006b__threshold_90_percent" b
						ON s."{{{ district_id_column }}}" = b.district_id
				LEFT JOIN "006c__threshold_95_percent" c
						ON s."{{{ district_id_column }}}" = c.district_id
				LEFT JOIN "006d__threshold_97_percent" d
						ON s."{{{ district_id_column }}}" = d.district_id
				LEFT JOIN "006e__proportional_90_percent" e
						ON s."{{{ district_id_column }}}" = e.district_id
				LEFT JOIN "006f__proportional_95_percent" f
						ON s."{{{ district_id_column }}}" = f.district_id
				LEFT JOIN "006g__proportional_97_percent" g
						ON s."{{{ district_id_column }}}" = g.district_id;
