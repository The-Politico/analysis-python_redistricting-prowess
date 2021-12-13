# https://www2.census.gov/programs-surveys/decennial/2020/data/01-Redistricting_File--PL_94-171/Rhode_Island/

# STATE_ABBR="ri"
STATE_ABBR="tx"

csvgrep \
  --delimiter "|" \
  --no-header-row \
  --columns "3" \
  --match "750" \
  --encoding "ISO-8859-1" \
  "${STATE_ABBR}geo2020.pl" | \
  csvcut --columns "8" |\
  sed 1d \
  >> 001__block-ids.txt


csvgrep \
  --delimiter "|" \
  --no-header-row \
  --columns "5" \
  --file "001__block-ids.txt" \
  "${STATE_ABBR}000012020.pl" |\
  sed 1d \
  >> 002__block-data-no-header.csv

echo -n "FILEID,STUSAB,CHARITER,CIFSN,LOGRECNO" \
  > 003__blocks-with-headers.csv && \
  echo -n ",P0010001,P0010002,P0010003,P0010004,P0010005,P0010006" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0010007,P0010008,P0010009,P0010010,P0010011,P0010012" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0010013,P0010014,P0010015,P0010016,P0010017,P0010018" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0010019,P0010020,P0010021,P0010022,P0010023,P0010024" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0010025,P0010026,P0010027,P0010028,P0010029,P0010030" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0010031,P0010032,P0010033,P0010034,P0010035,P0010036" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0010037,P0010038,P0010039,P0010040,P0010041,P0010042" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0010043,P0010044,P0010045,P0010046,P0010047,P0010048" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0010049,P0010050,P0010051,P0010052,P0010053,P0010054" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0010055,P0010056,P0010057,P0010058,P0010059,P0010060" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0010061,P0010062,P0010063,P0010064,P0010065,P0010066" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0010067,P0010068,P0010069,P0010070,P0010071" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0020001,P0020002,P0020003,P0020004,P0020005,P0020006" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0020007,P0020008,P0020009,P0020010,P0020011,P0020012" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0020013,P0020014,P0020015,P0020016,P0020017,P0020018" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0020019,P0020020,P0020021,P0020022,P0020023,P0020024" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0020025,P0020026,P0020027,P0020028,P0020029,P0020030" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0020031,P0020032,P0020033,P0020034,P0020035,P0020036" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0020037,P0020038,P0020039,P0020040,P0020041,P0020042" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0020043,P0020044,P0020045,P0020046,P0020047,P0020048" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0020049,P0020050,P0020051,P0020052,P0020053,P0020054" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0020055,P0020056,P0020057,P0020058,P0020059,P0020060" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0020061,P0020062,P0020063,P0020064,P0020065,P0020066" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0020067,P0020068,P0020069,P0020070,P0020071,P0020072" \
    >> 003__blocks-with-headers.csv && \
  echo -n ",P0020073" \
    >> 003__blocks-with-headers.csv && \
  echo "" \
    >> 003__blocks-with-headers.csv

cat 002__block-data-no-header.csv >> 003__blocks-with-headers.csv


csvcut \
  --columns "LOGRECNO,P0020001,P0020005" \
  003__blocks-with-headers.csv \
  >> 004__blocks_filtered.csv

csvstat --sum 004__blocks_filtered.csv > 005__statewide-sums.txt

# TODO: Join in the GEOID (the next column after LOGRECNO in the `<state>geo2020.pl` file) for easy spatial joining.
