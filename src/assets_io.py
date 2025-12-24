from .sheets_io import read_df


def read_assets():
    df = read_df("assets")

    asset_names = []
    risk_scores = []
    base_returns = []

    for _, row in df.iterrows():
        asset_names.append(str(row["Asset"]).strip())
        risk_scores.append(float(row["RiskScore"]))
        base_returns.append(float(row["BaseReturn"]))

    return asset_names, risk_scores, base_returns


