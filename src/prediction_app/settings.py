import os

MODEL_PATH = os.path.join("model", "hr_model.joblib")

HR_DATA_ENDPOINT = "https://hrv4roland.herokuapp.com/hrv"

DATETIME_FORMAT = "%Y-%m-%d %H:%M"

HR_DATA_COLS = ["hrpeak", "hrrest", "hrstanding", "hrvrest", "hrvstanding", "hours_from_hr_to_activity"]
