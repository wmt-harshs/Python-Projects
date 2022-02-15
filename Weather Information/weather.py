import requests
from pprint import pprint

API_key = "8453e84800b4f45af4ad2b799152ddbe"

city = input("Enter a city name:- ")

base_url = "api.openweathermap.org/data/2.5/weather?&appid=" + API_key + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)