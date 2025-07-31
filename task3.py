import requests
from pprint import pprint 

def get_weather():
    API_key = 'f7f73a807ab59c4f25be9ee95fbba6c5'
    url_kr = f'https://api.openweathermap.org/data/2.5/weather?id=524901&lang=kr&appid={API_key}'

    response = requests.get(url_kr).json()
    return response
    
get_weather()
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

def add_celsius_temps(data, translation):
    result = {}
    for k, v in data.items():
        kor_key = translation.get(k, k)
        if kor_key in ['온도', '최저온도', '최고온도', '체감온도']:
            if isinstance(v, (int, float)):
                result[f"{kor_key}(섭씨)"] = round(v - 273.15, 2)
    return result

result = get_weather()
main_kor = kor_keys(result.get("main", {}), key_kor)
main_celsius = add_celsius_temps( result.get("main", {}), key_kor)
weather_kor = kor_keys(result.get("weather", [{}])[0], key_kor)

# pprint(main_kor)
# pprint(weather_kor)

merge_kor_dict = {**main_kor, **main_celsius,**weather_kor}

pprint(merge_kor_dict)