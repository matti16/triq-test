from pydantic import BaseModel
from joblib import load
from typing import Optional

from .settings import MODEL_PATH
from .hr_data import HrData


class PredictionParams(BaseModel):
    username: str
    datetime: str


class PredictionResponse(BaseModel):
    prediction: bool
    message: Optional[str] = ""


class HrModel:
    def __init__(self, model_path=MODEL_PATH):
        """
        Initialize a model that works with Hearth Rate data
        :param model_path: path to the joblib file of the model
        """
        self.model = load(model_path)
        self.hr_data = HrData()

    def predict(self, params: PredictionParams) -> PredictionResponse:
        """

        :param params:
        :return:
        """
        features = self.hr_data.get_hr_data(params.username, params.datetime)
        prediction = bool(self.model.predict(features))
        return PredictionResponse(prediction=prediction)
