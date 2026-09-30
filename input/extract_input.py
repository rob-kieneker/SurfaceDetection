import pandas as pd


def extract_searcher_data() -> pd.DataFrame:
    return pd.read_json("input/searchers.json")


def extract_traveller_data() -> pd.DataFrame:
    return pd.read_json("input/travellers.json")
