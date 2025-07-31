import requests
from pprint import pprint 

def get_weather():
    API_key = 'f7f73a807ab59c4f25be9ee95fbba6c5'
    lat = 36.42
    lon = 127.00
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
 
    response = requests.get(url).json()
        
    return response

result = get_weather()

result1 = f'main: {result["main"]}, weather: {result["weather"]}, sys: {result["sys"]}'
pprint(result1)
