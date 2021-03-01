from fastapi import HTTPException


class PredictionNotAvailable(HTTPException):
    def __init__(self):
        super(PredictionNotAvailable, self).__init__(
            status_code=404,
            detail="Predictions for this user and datetime not available",
        )


class DataFetchError(HTTPException):
    def __init__(self):
        super(DataFetchError, self).__init__(
            status_code=500, detail="Service not available. Try again later."
        )
