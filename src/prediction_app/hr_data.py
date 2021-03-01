import requests
import pandas as pd
import datetime

from .exceptions import DataFetchError, PredictionNotAvailable
from .settings import HR_DATA_ENDPOINT, HR_DATA_COLS, HR_DATETIME_FORMAT

pd.options.mode.chained_assignment = None


class HrData:
    def __init__(self, endpoint=HR_DATA_ENDPOINT, datetime_format=HR_DATETIME_FORMAT):
        """
        Initialize an HrData class, used to request HR data to a specific endpoint.
        :param endpoint: Base URL that provides HR data
        """
        self.endpoint = endpoint
        self.datetime_format = datetime_format

    def get_hr_data(self, username: str) -> list:
        """
        Retrieve a list of HR data measurement for a given user, using an external endpoint.
        :param username: username for which we to retrieve data
        :return: the list of HR measurement retrieved from the endpoint
        """
        url = f"{self.endpoint}/?name={username}"

        try:
            data = requests.get(url, timeout=1.5)
        except requests.exceptions.RequestException:
            raise DataFetchError()

        if "data" in data.json():
            return data.json()["data"]
        else:
            raise PredictionNotAvailable()

    def pre_process_hr_data(self, data: list, datetime_str: str):
        """
        Pre-process the HR data to extract features to be used by the model.
        :param data: list of HR data measurements
        :param datetime_str: datetime string in the format specified in settings.
        :return:
        """
        df_hr = pd.DataFrame(data)
        df_hr["datetime"] = pd.to_datetime(df_hr["date"])
        request_datetime = datetime.datetime.strptime(datetime_str, self.datetime_format)
        df_features = df_hr[df_hr["datetime"] < request_datetime].sort_values(
            by="datetime", ascending=False
        )
        features = df_features.head(1)
        features["hours_diff"] = (request_datetime - features["datetime"]).dt.total_seconds() / 3600
        features = features[HR_DATA_COLS].values

        return features
