SELECT
  			s."{{{ district_num_column }}}" AS district,
				a.nonwhite_pct AS nonwhite_largestonly,
				b.nonwhite_pct AS nonwhite_threshold90,
				c.nonwhite_pct AS nonwhite_threshold95,
				d.nonwhite_pct AS nonwhite_threshold97,
				e.nonwhite_pct AS nonwhite_proportional90,
				f.nonwhite_pct AS nonwhite_proportional95,
				g.nonwhite_pct AS nonwhite_proportional97,
				a.bachelors_pct AS bachelors_largestonly,
				b.bachelors_pct AS bachelors_threshold90,
				c.bachelors_pct AS bachelors_threshold95,
				d.bachelors_pct AS bachelors_threshold97,
				e.bachelors_pct AS bachelors_proportional90,
				f.bachelors_pct AS bachelors_proportional95,
				g.bachelors_pct AS bachelors_proportional97
		INTO "106__compared_margins"
		FROM "105a__larger_coverage_wins" a
        INNER JOIN "{{{ district_shape_table }}}" s
            ON a.district_id = s."{{{ district_id_column }}}"
				INNER JOIN "105b__threshold_90_percent" b
						ON a.district_id = b.district_id
				INNER JOIN "105c__threshold_95_percent" c
						ON a.district_id = c.district_id
				INNER JOIN "105d__threshold_97_percent" d
						ON a.district_id = d.district_id
				INNER JOIN "105e__proportional_90_percent" e
						ON a.district_id = e.district_id
				INNER JOIN "105f__proportional_95_percent" f
						ON a.district_id = f.district_id
				INNER JOIN "105g__proportional_97_percent" g
						ON a.district_id = g.district_id;
