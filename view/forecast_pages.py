from flask import render_template, Blueprint, request


forecast_pages = Blueprint('forecast_pages', 'forecast_pages')


@forecast_pages.route('/forecast_page', methods=['get', 'post'])
def forecast_page():
    # location = request.values.get('location')
    # data = forecast_data(location)
    #
    # return render_template('forecast.html', T_min=int(data[0].get(u'tmp_min')), T_max=int(data[0].get(u'tmp_max')))
    return render_template('forecast.html')
