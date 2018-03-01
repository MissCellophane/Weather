from flask import render_template, Blueprint, request


forecast_pages = Blueprint('forecast_pages', 'forecast_pages')


@forecast_pages.route('/forecast_page', methods=['get', 'post'])
def forecast_page():
    print "1 from forecast_page"
    WEATHER = request.values.get('weather_data')
    return render_template('forecast.html', weather=WEATHER)