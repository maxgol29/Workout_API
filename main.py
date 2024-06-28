import requests
import datetime as dt
import os

date_now = dt.datetime.now()

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]


url = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params = {
    "query": f"{input('Tell me which exercises you did: ')}",
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 180,
    "age": 21
}

response = requests.post(url=url, headers=headers, json=params)
data = response.json()


docs_sheet_url = os.environ["docs_sheet_url"]
BEARER_AUTH = os.environ["BEARER_AUTH"]
header = {
    "Authorization": BEARER_AUTH
}

for activity in data["exercises"]:
    params = {
        "workout": {
            "date": date_now.strftime("%d/%m/%Y"),
            "time": date_now.strftime('%X'),
            "exercise": activity["user_input"].title(),
            "duration": activity["duration_min"],
            "calories": round(activity["nf_calories"]),
        }
    }
    response = requests.post(url=docs_sheet_url, json=params, headers=header)
    print(activity)
    print(response.json())


