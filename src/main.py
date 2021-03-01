from fastapi import FastAPI

from prediction_app.predictions import PredictionParams, PredictionResponse, HrModel
from prediction_app.settings import API_VERSION

app = FastAPI()

model = HrModel()


@app.post(f"/api/{API_VERSION}/predict")
def predict(params: PredictionParams) -> PredictionResponse:
    """
    Prediction endpoint.
    It accepts a JSON body containing username and datetime and returns a JSON response containing the prediction.
    :param params: PredictionParams with username and datetime
    :return: a PredictionResponse with the actual prediction (True for rest).
    """
    return model.predict(params)
