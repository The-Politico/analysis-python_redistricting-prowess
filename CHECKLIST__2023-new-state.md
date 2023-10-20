# Newly-enacted state checklist

0. Download the latest version of the raw data, with the `just download_data` command.

1. Download shapefile to raw_data/new_districts/<fips>/with_z/toEvaluate.shp

2. Add, then populate, the `dist_num` and `geoid` columns to the first shapefile. `dist_num` is a two-character zero padded string (01 to 52) of the district number. Meanwhile, `geoid` is a four-character string with the zero-padded state FIPS followed by the dist_num value.

3. Save this file, without the Z dimension, to ../z_sans_buffer/toEvaluate.shp

4. Run a zero-distance buffer on that shapefile, and save that out to ../toEvaluate.shp (with CRS 4326, if we didn't do this before)

5. Check that either precincts or census tracts (or both) are in the same place in QGIS — just to be sure the projections line up.

6. Open the PROWESS database on AWS, and see if any of the following exist, where `zz` is the lowercase two-letter postal abbreviation for the state you're processing:

- `prowess_v1_new__zz` (by default, this will be the political lean of the districts that were adopted before the 2022 elections)
- `prowess_v1_new__zz__census` (by default, this will be the demographics of the districts that were adopted before the 2022 elections)
- `prowess_v1_old__zz` (by default, this will be the political lean of the districts that were last used in 2020)
- `prowess_v1_old__zz__census` (by default, this will be the demographics of the districts that were last used in 2020)

You'll need to make sure the first two of these tables don't exist before proceeding with Step 7. But you may want to rename more than just those, so we've included all the per-state tables in this list.

7. Run the following, where XX is the state's FIPS code:

    ```python
    from analysis.political.runner import run_full_political_analysis

    a, b, c = run_full_political_analysis('XX', 'new')
    ```

8. Run the following, where XX is the state's FIPS code:

    ```python
    from analysis.demographic.runner import run_full_demographic_analysis

    a, b, c = run_full_demographic_analysis('XX', 'new')
    ```

9. Collect all the relevant data about new districts.

Again, where `zz` is the postal abbreviation for the state you're processing:

- `prowess_v1_new__zz` database -> `007__compared_margins` table -> `district` field [District number]
- `prowess_v1_new__zz` database -> `007__compared_margins` table -> `biden_proportional95` field [% of the two-party vote share won by Biden in 2020]
- `prowess_v1_new__zz__census` database -> `106__compared_margins` table -> `district` field [District number]
- `prowess_v1_new__zz__census` database -> `106__compared_margins` table -> `bachelors_proportional95` field [% of district residents age 25+ with bachelors' degrees]
- `prowess_v1_new__zz__census` database -> `106__compared_margins` table -> `nonwhite_proportional95` field [% of nonwhite voting-age district residents, including Hispanic/Latino identifying white residents]

To get the results from _old_ districts, repeat this process but use `prowess_v1_old__zz` and `prowess_v1_old__zz__census` instead.
