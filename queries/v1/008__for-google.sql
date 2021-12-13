WITH rounded_margins AS (
    SELECT
            district,
    				ROUND(CAST(biden_proportional90 AS numeric), 6) AS rounded90,
    				ROUND(CAST(biden_proportional95 AS numeric), 6) AS rounded95,
    				ROUND(CAST(biden_proportional97 AS numeric), 6) AS rounded97
        FROM "007__compared_margins"
)
SELECT
        district,
				ROUND(CAST(((rounded90 - 50) * 2) AS numeric), 3) AS prowess90,
				ROUND(CAST(((rounded95 - 50) * 2) AS numeric), 3) AS prowess95,
				ROUND(CAST(((rounded97 - 50) * 2) AS numeric), 3) AS prowess97
		INTO "008__for_google"
    FROM rounded_margins;
