import os
import json
import pandas as pd
from utilities import create_fred_client


class FredMetadataCollector:
    def __init__(self, series_file_path: str):
        self.series_file_path = series_file_path
        self.fred_client = create_fred_client()
        self.series = self.import_series_ids()

    def import_series_ids(self) -> dict:
        with open(self.series_file_path, "r") as file:
            data = json.load(file)
        return data

    def collect_metadata(self):
        results = []
        for id, series in self.series.items():
            data = (
                self.fred_client.search(id)
                .query(f"id == '{id}'")
                .drop(
                    columns=[
                        "id",
                        "realtime_start",
                        "realtime_end",
                        "frequency_short",
                        "units_short",
                        "seasonal_adjustment_short",
                        "notes",
                    ]
                )
            )
            data.insert(1, "name", series["name"])
            data.insert(2, "category", series["category"])
            results.append(data)
        return pd.concat(results, ignore_index=True)


if __name__ == "__main__":
    collector = FredMetadataCollector(
        os.path.join(os.getcwd(), "src/static/series.json")
    )
    fred_metadata = collector.collect_metadata()
    fred_metadata.to_csv(os.path.join(os.getcwd(), "src/data/fred_metadata.csv"))
