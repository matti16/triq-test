import requests
import pandas as pd
import datetime

from .settings import HR_DATA_ENDPOINT, HR_DATA_COLS, DATETIME_FORMAT


class HrData:
    def __init__(self, endpoint=HR_DATA_ENDPOINT):
        """

        :param endpoint:
        """
        self.endpoint = endpoint

    def get_hr_data(self, username: str, datetime_str: str):
        """

        :param datetime_str:
        :param username:
        :return:
        """

        url = f"{self.endpoint}/?name={username}"
        data = requests.get(url, timeout=1)
        request_datetime = datetime.datetime.strptime(datetime_str, DATETIME_FORMAT)
        df_hr = pd.DataFrame(data.json()['data'])
        df_hr["datetime"] = pd.to_datetime(df_hr["date"])
        df_features = df_hr[df_hr["datetime"] < request_datetime].sort_values(by="datetime", ascending=False)
        features = df_features.head(1)
        features["hours_from_hr_to_activity"] = (request_datetime - features["datetime"]).dt.seconds / 3600
        features = features[HR_DATA_COLS].values
        return features
