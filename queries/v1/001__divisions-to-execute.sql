WITH
		touching_precincts AS (
				SELECT
								p.county AS zfips,
								p.geoid AS precinct_id,
								d."{{{ district_num_column }}}" AS dist_num,
								d."{{{ district_id_column }}}" AS dist_geoid,
								p.geometry AS precinct_geom,
								d.geometry AS district_geom
						FROM "000a__precincts" p
								INNER JOIN "{{{ district_shape_table }}}" d
										ON ST_Intersects (p.geometry, d.geometry)
								WHERE p.county {{{ group_operator }}} {{{ group_counties_list }}}
    ),
		initial_division AS (
				SELECT
						dist_geoid,
		        precinct_id,
		        precinct_geom,
		        district_geom,
						ST_Intersection(precinct_geom, district_geom) AS overlap_geom
				FROM touching_precincts
		)
SELECT
				dist_geoid,
				precinct_id,
				(
						ST_Area(overlap_geom) / ST_Area(precinct_geom)
				) AS coverage,
				precinct_geom,
				district_geom,
				overlap_geom
		INTO "001{{{ group_letter }}}__divided_precincts_{{{ group_suffix }}}"
		FROM initial_division;
