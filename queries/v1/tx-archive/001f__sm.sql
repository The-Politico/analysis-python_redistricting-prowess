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
										-- SM (~34s)
										'323', '1', '199', '467',
										'401', '73', '265', '473',
										'325', '277', '13', '493',
										'349', '465', '373', '53',
										'499','259','55','143',
										'481','71','459','249',
										'97','49','321','223'
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
		INTO "001f__divided_precincts_sm"
		FROM initial_division
