import requests
from pprint import pformat

def get_weather():
    API_key = ''
    url_kr = f'https://api.openweathermap.org/data/2.5/weather?id=524901&lang=kr&appid={API_key}'
    response = requests.get(url_kr).json()
    return response

key_kor = {
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

main_data = result.get("main", {})
main_kor = kor_keys(main_data, key_kor)
main_celsius = add_celsius_temps(main_data, key_kor)
weather_data = result.get("weather", [{}])[0]
weather_kor = kor_keys(weather_data, key_kor)

output = (
    "[기온 정보]\n"
    f"{pformat({**main_kor, **main_celsius})}\n\n"
    "[날씨 설명]\n"
    f"{pformat(weather_kor)}"
)

print(output)
