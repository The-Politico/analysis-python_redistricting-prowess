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
								WHERE p.county NOT IN (
										-- XXS: all but the following (~44s)
										'201', '113', '439', '29',
										'453', '85', '215', '141',
										'121', '157', '339', '491',
										'61', '355', '39', '27',
										'167', '303', '479', '245',
										'309', '423', '41', '209',
										'139', '329', '251', '135',
										'187', '91', '441', '381',
										'367', '485', '181', '257',
										'183', '375', '451', '397',
										'231', '37', '469', '5',
										'21', '361', '291', '213',
										'99', '471', '409', '203',
										'497', '347', '427', '221',
										'323', '1', '199', '467',
										'401', '73', '265', '473',
										'325', '277', '13', '493',
										'349', '465', '373', '53',
										'499','259','55','143',
										'481','71','459','249',
										'97','49','321','223',
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
		INTO "001h__divided_precincts_xxs"
		FROM initial_division
