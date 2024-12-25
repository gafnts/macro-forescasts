import os
import json
import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv


def create_fred_client() -> Fred:
    load_dotenv()
    FRED_API_KEY = os.getenv("FRED_API_KEY")
    fred = Fred(api_key=FRED_API_KEY)
    return fred


def import_series_ids() -> dict[str, str]:
    with open(os.path.join(os.getcwd(), "series.json"), "r") as file:
        data = json.load(file)
    return data


def create_base_dataframe(
    start_date: str, end_date: str, frequency: str = "D"
) -> pd.DataFrame:
    if frequency not in ["D", "ME", "YE"]:
        raise ValueError(
            "Frequency must be 'D' for daily, 'ME' for monthly, or 'YE' for yearly."
        )

    date_range = pd.date_range(start=start_date, end=end_date, freq=frequency)
    df = pd.DataFrame(date_range, columns=["date"])

    if frequency == "ME":
        df["date"] = df["date"].dt.to_period("M").dt.to_timestamp()
    elif frequency == "Y":
        df["date"] = df["date"].dt.to_period("Y").dt.to_timestamp()

    return df


def extract_base_dataset(
    fred_client: Fred, series_ids: dict, base_df: pd.DataFrame
) -> pd.DataFrame:
    for id, name in series_ids.items():
        ts = fred_client.get_series(id, frequency='m', aggregation_method='avg')

        ts_df = (
            pd.DataFrame(ts, columns=[name])
            .reset_index()
            .rename(columns={"index": "date"})
        )

        base_df = base_df.merge(ts_df, on="date", how="left")
    return base_df
