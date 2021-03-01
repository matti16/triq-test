from pydantic import BaseModel, Field
from joblib import load

from .settings import MODEL_PATH
from .hr_data import HrData
from .exceptions import PredictionNotAvailable


class PredictionParams(BaseModel):
    username: str = Field(
        title="Username",
        description="Username for which you want predictions",
        min_length=1
    )
    datetime: str = Field(
        title="Datetime",
        description="Datetime for which you want predictions",
        regex=r"\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}"
    )


class PredictionResponse(BaseModel):
    prediction: bool
    hours_from_last_hr: float


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
        Predict if a user should rest or not at a given datetime.
        It gets the input data from HrData and calls self.model.predict.
        :param params: username and datetime string
        :return: A PredictionResponse with a boolean prediction and
                 the number of hours between the last HR measurement and the requested datetime
        """
        data = self.hr_data.get_hr_data(params.username)
        features = self.hr_data.pre_process_hr_data(data, params.datetime)

        if len(features):
            features = features[0]
            prediction = bool(self.model.predict([features]))
            hours_from_last_hr = features[-1]
            return PredictionResponse(
                prediction=prediction, hours_from_last_hr=hours_from_last_hr
            )
        else:
            raise PredictionNotAvailable()
