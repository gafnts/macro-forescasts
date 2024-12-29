from utilities import (
    create_fred_client,
    import_series_ids,
    create_base_dataframe,
    extract_base_dataset,
)


class Extractor:
    def __init__(self, start_date: str, end_date: str, frequency: str = "ME"):
        self.fred_client = create_fred_client()
        self.series_ids = import_series_ids()
        self.base_df = create_base_dataframe(start_date, end_date, frequency)
        self.data = None

    def extract_data(self):
        self.data = extract_base_dataset(
            fred_client=self.fred_client,
            series_ids=self.series_ids,
            base_df=self.base_df,
        )

    def save_to_csv(self, file_path: str):
        if self.data is not None:
            self.data.to_csv(file_path, index=False)
        else:
            raise ValueError("No data to save. Please run extract_data() first.")


if __name__ == "__main__":
    extractor = Extractor(
        start_date="1950-01-01", end_date="2025-01-01", frequency="ME"
    )
    extractor.extract_data()
    extractor.save_to_csv("./src/data/raw.csv")
