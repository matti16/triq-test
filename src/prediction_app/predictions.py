from fastapi import HTTPException
from pydantic import BaseModel
from joblib import load
from typing import Optional

from prediction_app.settings import MODEL_PATH


class PredictionParams(BaseModel):
    username: str
    datetime: str


class PredictionResponse(BaseModel):
    rest: bool
    message: Optional[str] = ""


class HrModel:
    def __init__(self, model_path=MODEL_PATH):
        """
        Initialize a model that works with Hearth Rate data
        :param model_path: path to the joblib file of the model
        """
        self.model = load(model_path)

    def predict(self, params: PredictionParams) -> PredictionResponse:
        return PredictionResponse(rest=False)
