import json
import pandas as pd


class HandleJson:
    def create_json(self, filename):
        with open(filename, "w") as file:
            file.write("{}")
        file.close()

    def get_json_data_to_dataframe(self, filename):
        """
        Reads a JSON file from the "data_samples" directory, normalizes it using pandas,
        and returns the resulting dataframe.
        Args:
            filename (str): The name of the JSON file to read.
        Returns:
            pandas.DataFrame: A normalized dataframe representing the data in the JSON file.
        """
        data = json.load(open(filename))
        df = pd.json_normalize(data)
        return df

    def add_to_dataframe(self, df, cmd):
        cmd = cmd.split(" ")[0]
        if cmd in df:
            df[cmd] += 1
        else:
            df[cmd] = 1

    def df_to_json(self, df, filename):
        df.to_json(filename, orient="records")
