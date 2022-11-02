import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv('WEATHER_API_KEY')


def kelvin_to_celsius(temp_k):
    return round(temp_k - 273.15, 1)


city = input("Enter municipality name: ").title()
request = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        # print(json.dumps(json_response, indent=1))
        cur_temp = json_response["main"]["temp"]
        cur_weather = json_response["weather"][0]["description"]
        cur_weather_feels = json_response["main"]["feels_like"]
        print(f"Currently it's {cur_weather} in {city} with temperature {kelvin_to_celsius(cur_temp)} C. "
              f"\nFeels like {kelvin_to_celsius(cur_weather_feels)} C.")
except requests.exceptions.RequestException as e:
    print("Request could not be completed")











