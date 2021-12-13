SELECT *
  INTO  "002__concatenated"
  FROM "001a__divided_precincts_xxl_1";

INSERT INTO  "002__concatenated"
  SELECT *
  FROM "001b__divided_precincts_xxl_2";

INSERT INTO  "002__concatenated"
  SELECT *
  FROM "001c__divided_precincts_xl";

INSERT INTO  "002__concatenated"
  SELECT *
  FROM "001d__divided_precincts_lg";

INSERT INTO  "002__concatenated"
  SELECT *
  FROM "001e__divided_precincts_md";

INSERT INTO  "002__concatenated"
  SELECT *
  FROM "001f__divided_precincts_sm";

INSERT INTO  "002__concatenated"
  SELECT *
  FROM "001g__divided_precincts_xs";

INSERT INTO  "002__concatenated"
  SELECT *
  FROM "001h__divided_precincts_xxs";
