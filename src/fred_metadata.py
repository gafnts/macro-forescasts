import os
import json
import pandas as pd
from tqdm import tqdm
from utilities import create_fred_client


class FredMetadataCollector:
    def __init__(
        self, series_file_path: str, frequencies_file_path: str, units_file_path: str
    ):
        self.fred_client = create_fred_client()

        self.series_file_path = series_file_path
        self.frequencies_file_path = frequencies_file_path
        self.units_file_path = units_file_path

        self.series = self.import_json(self.series_file_path)
        self.frequencies = self.import_json(self.frequencies_file_path)
        self.units = self.import_json(self.units_file_path)

    @staticmethod
    def import_json(file_path: str) -> dict:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data

    def collect_metadata(self):
        results = []
        for id, series in tqdm(
            self.series.items(), desc="Collecting FRED series metadata"
        ):
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

    def process_metadata(self, metadata: pd.DataFrame) -> pd.DataFrame:
        metadata["frequency"] = metadata["frequency"].map(self.frequencies)
        metadata["units"] = metadata["units"].map(self.units)
        return metadata


if __name__ == "__main__":
    collector = FredMetadataCollector(
        os.path.join(os.getcwd(), "src/static/fred/series.json"),
        os.path.join(os.getcwd(), "src/static/fred/frequencies.json"),
        os.path.join(os.getcwd(), "src/static/fred/units.json"),
    )
    fred_metadata = collector.collect_metadata()
    processed_metadata = collector.process_metadata(fred_metadata)
    processed_metadata.to_csv(os.path.join(os.getcwd(), "src/data/metadata/fred.csv"))
