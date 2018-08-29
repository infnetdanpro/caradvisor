import requests

from settings import OPENWEATHER_API_KEY

URL_CURRENT_WEATHER = 'http://api.openweathermap.org/data/2.5/weather?id=524901&units=metric&lang=ru&appid=%s' % (OPENWEATHER_API_KEY)
URL_WEATHER_FORECAST_FOR_SIX_HOURS = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&units=metric&lang=ru&appid=%s' % (OPENWEATHER_API_KEY)

def get_weather_data(url):
    """Getting current weather json data"""
    try:
        result = requests.get(url)
    except requests.exceptions.RequestException as e:
        print('Exception happend: ', e)

    if result.status_code == 200:
        return result.json()
    else:
        print('Something is wrong with server response')


def get_current_weather_message():
    """Returns current weather conditions message"""
    data = get_weather_data(URL_CURRENT_WEATHER)
    current_weather_message = ''
    current_weather_message += 'Тек. t = {} \xB0C '.format(data['main']['temp'])
    current_weather_message += '(Max = {} \xB0С, '.format(data['main']['temp_max'])
    current_weather_message += 'Min = {} \xB0C)'.format(data['main']['temp_min'])
    current_weather_message += '\nПогодные усл. - {}, '.format(data['weather'][0]['description'])
    current_weather_message += 'видимость - {} м\n '.format(data['visibility'])
    current_weather_message += 'Ветер - {} м/с, '.format(data['wind']['speed'])
    current_weather_message += 'облачность {}%'.format(data['clouds']['all'])
    return current_weather_message


def get_weather_forecast_for_six_hours():
    """Returns weather forecast message for 6 hours ahead"""
    weather_forecast_data = get_weather_data(URL_WEATHER_FORECAST_FOR_SIX_HOURS)

    weather_forecast_for_six_hours_message = 'Прогноз погоды на 9 часов:\n'
    for weather_forecast in weather_forecast_data['list'][1:5]:
        weather_forecast_for_six_hours_message += '{} '.format(weather_forecast['dt_txt'])
        weather_forecast_for_six_hours_message += 't = {}\xB0C '.format(weather_forecast['main']['temp'])
        weather_forecast_for_six_hours_message +=  '{} \n'.format(weather_forecast['weather'][0]['description'])
    return weather_forecast_for_six_hours_message


if __name__ == '__main__':
    print(get_current_weather_message())
    print(get_weather_forecast_for_six_hours())
