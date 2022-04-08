# Python-Projects-Get-Weather-Data 🐍
Python Script <br>
This repo contains python code that collects weather data about any city in the world. <br>
Run the code.

Python
```python
import requests
from pprint import pprint

API_Key = ''

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)
```

Output
```python
Enter a city: London
{'base': 'stations',
 'clouds': {'all': 99},
 'cod': 200,
 'coord': {'lat': 51.5085, 'lon': -0.1257},
 'dt': 1631937768,
 'id': 2643743,
 'main': {'feels_like': 286.62,
          'humidity': 92,
          'pressure': 1014,
          'temp': 286.8,
          'temp_max': 288.82,
          'temp_min': 283.53},
 'name': 'London',
 'sys': {'country': 'GB',
         'id': 2019646,
         'sunrise': 1631943620,
         'sunset': 1631988544,
         'type': 2},
 'timezone': 3600,
 'visibility': 6000,
 'weather': [{'description': 'overcast clouds',
              'icon': '04n',
              'id': 804,
              'main': 'Clouds'}],
 'wind': {'deg': 0, 'speed': 1.03}}



```
