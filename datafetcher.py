import json


class DataFetcher:
    def __init__(self):
        pass

    def getJson(self, filename):
        with open(filename) as file:
            return json.load(file)
