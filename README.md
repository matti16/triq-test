# Triq Test

This app provides a simple model to predict if a user should rest on a given day, using hearth rate data.


## Setup

The application is a web server implemented using FastAPI.

It can be deployed either using Docker or directly on the machine. 

#### Docker
```shell script
docker build -t triq-test .
docker run -d --name triq-test -p 80:80 triq-test
```

#### Local Machine
It is recommended to run this inside a Python virtual environment.
```shell script
pip install -r requirements.txt
cd src
uvicorn main:app --port 80
```

## Predictions
If the setup is successful, you should be able to get predictions for a given user and datetime.

Here an example of request:
```shell script
curl --location --request POST 'http://127.0.0.1:80/api/v1/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "Bob",
    "datetime": "2020-08-15 10:00"
}'
```  

**N.B.** It could take some time to get a 200 response, since it relies on an external API endpoint on Heroku, that needs to warm up.

The response is a JSON that contains a _**prediction**_ field (true in case the user should rest).

It also contains the number of hours between the last HR measurement available and the datetime of the prediction.

```json
{
    "prediction": true,
    "hours_from_last_hr": 3.183333333333333
}
```

## Model
In the _notebooks_ folder, there is an iPython notebook with some data analysis and the process used to build the simple model that powers the application.