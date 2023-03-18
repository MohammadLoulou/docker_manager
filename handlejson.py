import json
import pandas as pd
from os import path


class HandleJson:
    def open_json(self, filename):
        exists = False
        if path.exists(filename):
            exists = True
        with open(filename, "a") as file:
            if exists == False:
                file.write("{}")
        file.close()

    def json_data_to_dataframe(self, filename):
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
        if isinstance(df.squeeze(), pd.Series):
            df = df.squeeze()
        else:
            df = pd.Series(df.iloc[0])
        df.to_json(filename)
