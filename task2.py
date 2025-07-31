import requests
from pprint import pprint 

def get_weather():
    API_key = 'f7f73a807ab59c4f25be9ee95fbba6c5'
    url_kr = f'https://api.openweathermap.org/data/2.5/weather?id=524901&lang=kr&appid={API_key}'

    response = requests.get(url_kr).json()
        
    return response

key_kor = {
    'main': '기본',
    'temp': '온도',
    'temp_min' : '최저온도',
    'temp_max' : '최고온도',
    'feels_like': '체감온도',
    'pressure' : '기압',
    'humidity' : '습도',
    'weather': '날씨',
    'id': '식별자',
    'main': '핵심',
    'description': '요약',
    'icon': '아이콘'
}
def kor_keys(data, translation):
    return {translation.get(k, k): v for k, v in data.items()}

result = get_weather()
main_kor = kor_keys(result.get("main", {}), key_kor)

weather_kor = kor_keys(result.get("weather", [{}])[0], key_kor)

pprint(main_kor)
pprint(weather_kor)

