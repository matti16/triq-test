from fastapi import FastAPI

from prediction_app.predictions import PredictionParams, HrModel

# initiate API
app = FastAPI()

model = HrModel()


@app.post("/predict")
def predict(params: PredictionParams):
    """
    Prediction endpoint
    :param params: username and datetime for which we want the prediction
    :return: True if the model predicts rest, false otherwise
    """
    return model.predict(params)
