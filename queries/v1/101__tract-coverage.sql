WITH
		touching_precincts AS (
				SELECT
								t."GEOID" AS tract_id,
								d."{{{ district_num_column }}}" AS dist_num,
								d."{{{ district_id_column }}}" AS dist_geoid,
								t.geometry AS tract_geom,
								d.geometry AS district_geom
						FROM "000d__tract_geographies" t
								INNER JOIN "{{{ district_shape_table }}}" d
										ON ST_Intersects (t.geometry, d.geometry)
    ),
		initial_division AS (
				SELECT
						dist_geoid,
		        tract_id,
		        tract_geom,
		        district_geom,
						ST_Intersection(tract_geom, district_geom) AS overlap_geom
				FROM touching_precincts
		)
SELECT
				dist_geoid,
				tract_id,
				(
						ST_Area(overlap_geom) / ST_Area(tract_geom)
				) AS coverage,
				tract_geom,
				district_geom,
				overlap_geom
		INTO "101__tract_coverages"
		FROM initial_division;
