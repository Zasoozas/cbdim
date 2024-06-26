from pyowm import OWM
from pyowm.utils.config import get_default_config

def get_weather(city):
    owm = OWM("8aaf524ab172137da7ea9b2e772aab8c")

    config_dict = get_default_config()
    config_dict["language"] = "ru"
    manager = owm.weather_manager()
    observation = manager.weather_at_place(city)
    weather = observation.weather
    temp = weather.temperature("celsius")
    return f"Погода: {weather.detailed_status}\n" \
           f"Температура: {int(temp['temp'])}°C\n" \
           f"Ощущается: {int(temp['feels_like'])}°C\n" \
           f"Влажность: {weather.humidity}%\n" \
           f"Облачность: {weather.clouds}%\n"

if __name__ == "__main__":
    print(get_weather("Москва"))