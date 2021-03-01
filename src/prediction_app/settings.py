import os

API_VERSION = "v1"

MODEL_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "model", "hr_model.joblib")

HR_DATA_ENDPOINT = os.getenv("HR_DATA_ENDPOINT", "https://hrv4roland.herokuapp.com/hrv")

HR_DATETIME_FORMAT = "%Y-%m-%d %H:%M"

HR_DATA_COLS = [
    "hrpeak",
    "hrrest",
    "hrstanding",
    "hrvrest",
    "hrvstanding",
    "hours_diff",
]
