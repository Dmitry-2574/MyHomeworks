
from urllib import response
import requests
from plyer import notification
url = r'https://api.openweathermap.org/data/2.5/weather?q=Москва&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru'

response = requests.get(url)
# print(response.status_code)
# print(response.json())
weather_dict = response.json()
# Константы
API_KEY = "23496c2a58b99648af590ee8a29c5348"  # Используйте свой ключ API
CITY = "Moscow"

def get_weather(city: str, api_key: str) ->dict:
    url = fr'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'
    response = requests.get(url)
    return response.json()
    
def format_weather_message(weather_dict: dict) ->str:
    temp = weather_dict['main']['temp']
    feels_like = weather_dict['main']['feels_like']
    description = weather_dict['weather'][0]['description']
    return f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}'

def notify_weather(message:str) -> None:

    notification.notify(
    title=f'Погода в {CITY}',
    message=message,
    app_name='My Weather App',
    app_icon=None)

def main():
    """Запускает программу."""
    weather_data = get_weather(CITY, API_KEY)
    weather_message = format_weather_message(weather_data)
    notify_weather(weather_message)
    print(weather_message) #вывод в консоль


if __name__ == "__main__":
    main()
