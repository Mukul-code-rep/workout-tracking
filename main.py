import requests
import os
import datetime as dt

APP_ID = os.environ.get("ID")
APP_KEY = os.environ.get("KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/94925d68e9e0e5f699c16eaf7578e9ef/copyOfMyWorkout/sheet1"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}
parameters = {
    "query": input("What did you do?\n"),
    "gender": "male"
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
data = response.json()

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": "Bearer randomtoken"
}

for i in range(len(data["exercises"])):
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": data["exercises"][i]["name"],
            "duration": data["exercises"][i]["duration_min"],
            "calories": data["exercises"][i]["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=bearer_headers)
    sheet_response.raise_for_status()
    print(sheet_response.text)
# print(len(data['exercises']))
