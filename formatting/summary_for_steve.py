# Imports from python.
import csv
from pathlib import Path


# Imports from other dependencies.
import us


# Imports from PROWESS.
from formatting.state_detail import EMPTY_DATAFRAME
from formatting.state_detail import load_state_data


OUTPUT_DIR = "outputs/for-steve"


def generate_summary_lists():
    all_districts = dict(
        old=[],
        new=[],
    )

    for state in us.states.STATES:
        state_abbr = state.abbr.lower()

        state_data = load_state_data(state_abbr)

        old_voting_data = state_data.get("old", {}).get(
            "voting", EMPTY_DATAFRAME
        )
        new_voting_data = state_data.get("new", {}).get(
            "voting", EMPTY_DATAFRAME
        )

        if not old_voting_data.empty:
            all_districts["old"].extend(
                [
                    dict(
                        full_district="-".join(
                            [state_abbr.upper(), district_record["district"]]
                        ),
                        bidenMargin95=district_record["biden_proportional95"],
                    )
                    for district_record in old_voting_data.to_dict("records")
                ]
            )
        else:
            print(f"SKIPPING OLD STATE '{state_abbr.upper()}'...")

        if not new_voting_data.empty:
            all_districts["new"].extend(
                [
                    dict(
                        full_district="-".join(
                            [state_abbr.upper(), district_record["district"]]
                        ),
                        bidenMargin95=district_record["biden_proportional95"],
                    )
                    for district_record in new_voting_data.to_dict("records")
                ]
            )
        else:
            print(f"SKIPPING NEW STATE '{state_abbr.upper()}'...")

    # Sort old & new data by lowest to highest Biden margin.
    sorted_old = sorted(all_districts["old"], key=lambda x: x["bidenMargin95"])
    sorted_new = sorted(all_districts["new"], key=lambda x: x["bidenMargin95"])

    # Create output dir, if it doesn't exist.
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    # Format and export old data.
    old_output_file = f"{OUTPUT_DIR}/old.csv"
    with open(old_output_file, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=sorted_old[0].keys())

        writer.writeheader()

        for data_row in sorted_old:
            writer.writerow(data_row)

    # Format and export new data.
    new_output_file = f"{OUTPUT_DIR}/new.csv"
    with open(new_output_file, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=sorted_new[0].keys())

        writer.writeheader()

        for data_row in sorted_new:
            writer.writerow(data_row)

    return [old_output_file, new_output_file]
