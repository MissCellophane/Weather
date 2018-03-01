from const import hweather_api, LANG, UNIT, KEY
import requests


def forecast_data(LOCATION):
    parameters = {"location": LOCATION,
                  "key": KEY,
                  "lang": LANG,
                  "unit": UNIT}
    result = requests.get(hweather_api, params=parameters)
    data = result.json()["HeWeather6"][0]["daily_forecast"]
    return data

