import requests
from datetime import datetime
import os

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]
SHEET_AUTH = os.environ["SHEET_AUTH"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]

exercise_text = input("Tell me which exercises you did: ")

GENDER = "male"
WEIGHT = 76.5
HEIGHT = 174.2
AGE = 21

exercise_data = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=f"{EXERCISE_ENDPOINT}", json=exercise_data, headers=headers)
results = response.json()
exercises = results["exercises"]

today = datetime.now()
today_date = today.date().strftime("%d/%m/%Y")
today_time = today.time().strftime("%X")

for exercise in exercises:
    sheet_data = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(url=f"{SHEET_ENDPOINT}", json=sheet_data, auth=(USERNAME, PASSWORD))
    print(response.text)
