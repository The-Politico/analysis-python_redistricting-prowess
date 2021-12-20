# Newly-enacted state checklist

0. Download the latest version of the raw data, with the `just download_data` command.

1. Download shapefile to raw_data/new_districts/<fips>/with_z/toEvaluate.shp

2. Add the `dist_num` and `geoid` columns to the first shapefile.

3. Save this file, without the Z dimension, to ../z_sans_buffer/toEvaluate.shp

4. Run a zero-distance buffer on that shapefile, and save that out to ../toEvaluate.shp (with CRS 4326, if we didn't do this before)

5. Check that either precincts or 2020 districts (or both) are in the same place in QGIS

6. Run the following, where XX is the state's FIPS code:

    ```python
    from analysis.political.runner import run_full_political_analysis

    a, b, c = run_full_political_analysis('XX', 'new')
    ```

7. Run the following, where XX is the state's FIPS code:

    ```python
    from analysis.demographic.runner import run_full_demographic_analysis

    a, b, c = run_full_demographic_analysis('XX', 'new')
    ```

8. Add the state's precursor config to `./config/precursors.py`.
9. Add any new copy to the Kitchensink doc.
10. Run the following, where XX is the state's FIPS code:

    ```python
    from formatting.overall_commands import rebake_single_state

    ff = rebake_single_state('XX')
    ```

11. Finally, update your data on S3 using the `just upload_data` command.
