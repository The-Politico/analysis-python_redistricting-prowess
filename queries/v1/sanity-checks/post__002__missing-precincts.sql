-- Should yield zero rows.

WITH concat_precincts AS (
	SELECT DISTINCT ON (precinct_id) precinct_id FROM "002__concatenated"
), orig_precincts AS (
	SELECT
			DISTINCT ON ("PCTKEY")
			"PCTKEY" AS precinct_id,
			"G20PRERTRU" AS trump,
			"G20PREDBID" AS biden,
			(
				 COALESCE("G20PRERTRU", 0) + COALESCE("G20PREDBID", 0) +
				 COALESCE("G20PRELJOR", 0) + COALESCE("G20PREGHAW", 0) +
				 COALESCE("G20PREOWRI", 0)
			) AS all_potus,
			geometry
		FROM "000a__precincts"
)
SELECT
		o.*
	INTO sanity__bad_precincts
	FROM orig_precincts o
  LEFT OUTER JOIN concat_precincts c
		ON o.precinct_id = c.precinct_id
	WHERE c IS NULL;
