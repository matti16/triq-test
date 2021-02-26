from fastapi import HTTPException


class PredictionNotAvailable(HTTPException):
    def __init__(self):
        super(PredictionNotAvailable, self).__init__(status_code=404,
                                                     detail="Predictions for this user and datetime not available")


class PredictionError(HTTPException):
    def __init__(self):
        super(PredictionError, self).__init__(status_code=500,
                                              detail="Error while computing predictions for given user and datetime")
