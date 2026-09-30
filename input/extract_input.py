import pandas as pd


def extract_searcher_data() -> pd.DataFrame:
    return pd.read_json(
        "input/searchers.json", dtype={"model": str, "speed": float, "endurance": float}
    )


def extract_traveller_data() -> pd.DataFrame:
    return pd.read_json(
        "input/travellers.json",
        dtype={"model": str, "speed": float, "endurance": float, "arrival_rate": float},
    )
