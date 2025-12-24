from .sheets_io import read_df


def read_constraints():
    df = read_df("Constraints")

    global_constraints = {}
    asset_limits = {}

    asset_section_started = False

    for _, row in df.iterrows():
        key = row.iloc[0]
        val1 = row.iloc[1]
        val2 = row.iloc[2] if len(row) > 2 else None

        if str(key).strip() == "":
            continue

        if str(key).strip() == "Asset":
            asset_section_started = True
            continue

        if not asset_section_started:
            global_constraints[str(key).strip()] = val1
        else:
            asset_limits[str(key).strip()] = {
                "min": float(val1),
                "max": float(val2)
            }

    return global_constraints, asset_limits
