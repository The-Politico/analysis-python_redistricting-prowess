SELECT *
    INTO "004a__majorities_only"
    FROM "003__with_results"
    WHERE coverage > 0.5;
