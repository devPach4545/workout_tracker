import requests
from datetime import datetime
import os

# Get the current date and time
today = datetime.now()
today_date = today.strftime("%m/%d/%y")
today_time = today.strftime("%X")

# Prepare headers with API credentials
head = {
    "x-app-id" : os.environ.get("APP_ID"),
    "x-app-key" : os.environ.get("API_KEY"),
}

# API endpoint for exercise tracking
endpoint_1 = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Input exercise data
exercise_data_1 = {
    "query": input("what did you do?: "),
    "gender":"male",
    "weight_kg":66,
    "height_cm":180,
    "age":21,
}

# Make a POST request to the exercise tracking API
response = requests.post(headers=head, url=endpoint_1, json=exercise_data_1)
data = response.json()

# Extract exercise details from the response
data_exercise = response.json()["exercises"][0]['user_input']
data_duration = response.json()["exercises"][0]['duration_min']
data_calories = response.json()["exercises"][0]['nf_calories']

# Prepare input data for the sheet
sheet_inputs = {
    "sheet1": {
        "date": today_date,
        "time": today_time,
        "exercise": data_exercise.title(),
        "duration": data_duration,
        "calories": data_calories,
    }
}

# Fetch Sheety credentials from environment variables
env_user_name = os.environ.get("SHEETY_USERNAME")
env_password = os.environ.get("PASSWORD_SHEETY")
env_endpoint = os.environ.get("SHEETY_ENDPOINT")

# Make a POST request to Sheety API to add data to the sheet
sheet_response = requests.post(auth=(env_user_name, env_password), url=env_endpoint, json=sheet_inputs)
