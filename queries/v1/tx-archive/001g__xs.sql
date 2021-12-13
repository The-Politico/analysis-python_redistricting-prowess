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
										-- XS (~31s)
										'227','217','241','477',
										'147', '189', '449', '25',
										'273', '67', '15', '363',
										'407', '185', '463', '171',
										'419', '149', '331', '7',
										'293', '365', '219', '225',
										'179', '19', '57', '489',
										'457', '341', '233', '89',
										'299', '281', '177', '165',
										'123', '285', '253', '163',
										'161', '337', '117', '35',
										'133', '51', '503', '03'
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
		INTO "001g__divided_precincts_xs"
		FROM initial_division
