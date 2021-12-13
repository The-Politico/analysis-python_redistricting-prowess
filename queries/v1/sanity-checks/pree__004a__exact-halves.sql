-- Should yield zero rows.

SELECT *
    INTO "sanity__exact_halves"
    FROM "003__with_results"
    WHERE coverage = 0.5;
