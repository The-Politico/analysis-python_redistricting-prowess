WITH
		touching_precincts AS (
				SELECT
								p.county AS zfips,
								p.geoid AS precinct_id,
								o."CD116FP" AS dist_num,
								o."GEOID" AS dist_geoid,
								p.geometry AS precinct_geom,
								o.geometry AS old_dist_geom
						FROM "000a__precincts" p
								INNER JOIN "000b__old_districts" o
										ON ST_Intersects (p.geometry, o.geometry)
								WHERE p.county IN (
										-- MD (~38s)
										'187', '91', '441', '381',
										'367', '485', '181', '257',
										'183', '375', '451', '397',
										'231', '37', '469', '5',
										'21', '361', '291', '213',
										'99', '471', '409', '203',
										'497', '347', '427', '221'
							)
    ),
		initial_division AS (
				SELECT
						dist_geoid,
		        precinct_id,
		        precinct_geom,
		        old_dist_geom,
						ST_Intersection(precinct_geom, old_dist_geom) AS overlap_geom
				FROM touching_precincts
		)
SELECT
				dist_geoid,
				precinct_id,
				(
						ST_Area(overlap_geom) / ST_Area(precinct_geom)
				) AS coverage,
				precinct_geom,
				old_dist_geom,
				overlap_geom
		INTO "001e__divided_precincts_md"
		FROM initial_division
