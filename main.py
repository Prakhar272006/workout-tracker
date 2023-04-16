import os
import requests
from datetime import datetime
APP_ID = "113bd11d"
KEY = "570f59ddb280bafd1faf515cdd05645c"

gender = "male"
age = 16
height = 151.69
weight = 50.25


exercise_endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("What exercise yo did today?\n")

header = {
    "x-app-id" : APP_ID,
    "x-app-key" : KEY,
    # "x-remote-user-id":0

}
data = {
 "query":exercise_input,
 "gender":gender,
 "weight_kg":weight,
 "height_cm":height,
 "age":age

}

response = requests.post(url=exercise_endpoint,json=data,headers=header)
result = response.json()

sheet_api_endpoint = "https://api.sheety.co/59ad9266b3f80f6c3cfa2569c21807b6/copyOfMyWorkouts/workouts"
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_data = {
        "workout":{
                "date": today_date,
                "time": now_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
        }
    }
auth =("prakhargurjar27","prakhargurjar12345")
sheet_response = requests.post(url=sheet_api_endpoint,json=sheet_data,auth=auth)
print(f"your response has been added. please go and check it on : https://docs.google.com/spreadsheets/d/1jRqZ-MLaQSN6gjS8DBvZica73Iwu1xKNk8yRJZ5P13c/edit#gid=0")
