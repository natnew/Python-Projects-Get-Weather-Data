import requests
from pprint import pprint

API_Key = 'e42c46439103fff331866f0f00e0289c'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)

