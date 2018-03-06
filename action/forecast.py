from const import hweather_api, LANG, UNIT, KEY, CONDITIONS
import requests, json
from action.login_check import users


def add_to_pref(uid, cities):
    users.find_one_and_update({'uid': uid}, {"$set": {'ucity': cities}})


def preference(uid, cities):
    print 'cities', cities
    for city in cities:
        parameters = {"location": city,
                      "key": KEY,
                      "lang": LANG,
                      "unit": UNIT}
        r = requests.get(hweather_api, params=parameters)
        res = r.json()
        result = res['HeWeather6'][0]
        if result['status'] == 'unknown city':
            return 0

        add_to_pref(uid, cities)

    return 1


def default_cities(uid):
    result = users.find_one({'uid': uid})
    if not ('ucity' in result):
        return []
    cities = result['ucity']
    return cities


def forecast_data(uid):
    user = users.find_one({'uid': uid})
    cities = user['ucity']

    loc = {}
    for LOCATION in cities:
        parameters = {"location": LOCATION,
                      "key": KEY,
                      "lang": LANG,
                      "unit": UNIT}
        r = requests.get(hweather_api, params=parameters)
        ret = r.json()
        res = ret['HeWeather6'][0]
        result = res.get('daily_forecast', {})
        data = []
        for day in result:
            daily = {}
            for key in CONDITIONS:
                daily[key] = day[CONDITIONS[key]]

            data.append(daily)

        loc[LOCATION] =data


    return loc

