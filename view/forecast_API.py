from action.forecast import forecast_data
from flask import request, jsonify, Blueprint

forecast_apis = Blueprint('forecast_apis', 'forecast_apis')


@forecast_apis.route('/forecast', methods=['get', 'post'])
def forecast_fetch_data():
    return jsonify(weather_data=unicode(forecast_data(request.values.get('location'))))

