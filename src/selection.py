import os
import json
import pandas as pd
from utilities import create_fred_client


class SeriesProcessor:
    def __init__(self, series_file_path: str):
        self.series_file_path = series_file_path
        self.fred_client = create_fred_client()
        self.series = self.import_series()

    def import_series(self) -> dict:
        with open(self.series_file_path, "r") as file:
            data = json.load(file)
        return data

    def process_series(self):
        results = []
        for key, value in self.series.items():
            data = (
                self.fred_client.search(key)
                .query(f"id == '{key}'")
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
            data.insert(1, "name", value["name"])
            data.insert(2, "category", value["category"])
            results.append(data)
        return pd.concat(results, ignore_index=True)


if __name__ == "__main__":
    processor = SeriesProcessor(os.path.join(os.getcwd(), "src/static/series.json"))
    processed_data = processor.process_series()
    processed_data.to_csv(os.path.join(os.getcwd(), "src/data/test.csv"))
