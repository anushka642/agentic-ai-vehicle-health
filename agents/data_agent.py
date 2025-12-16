import pandas as pd

class DataAgent:
    def get_latest_data(self):
        df = pd.read_csv(
            "data/telemetry.csv",
            encoding="latin1",
            on_bad_lines="skip"
        )
        return df.iloc[0]
