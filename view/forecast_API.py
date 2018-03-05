from action.forecast import forecast_data, preference, default_cities
from flask import request, jsonify, Blueprint
import json

forecast_apis = Blueprint('forecast_apis', 'forecast_apis')


@forecast_apis.route('/forecast', methods=['get', 'post'])
def forecast_fetch_data():
    uid = request.values.get('uid')
    print '----forecast_fetch_data'
    print 'uid', uid
    weather_data = forecast_data(uid)
    return jsonify(weather_data=weather_data)


@forecast_apis.route('/forecast_preference', methods=['get', 'post'])
def forecast_preference():
    cities = request.values.get('pref')
    lists = json.loads(cities)
    uid = request.values.get('uid')
    print '----forecast_preference'
    print 'list', lists
    result = preference(uid, lists)
    return jsonify(status=result)


@forecast_apis.route('/forecast_setdefault', methods=['get', 'post'])
def forecast_default():
    uid = request.values.get('uid')
    result = default_cities(uid)
    return jsonify(cities=result)

