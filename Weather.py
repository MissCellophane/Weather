from flask import Flask, render_template
app = Flask(__name__)
app.secret_key = 'Nothing is wrong!'

from view.login_API import apis
from view.login_pages import pages
from view.forecast_API import forecast_apis
from view.forecast_pages import forecast_pages

app.register_blueprint(apis, url_prefix='/apis')
app.register_blueprint(pages, url_prefix='')
app.register_blueprint(forecast_apis, url_prefix='/apis')
app.register_blueprint(forecast_pages, prefix='')


@app.route('/index')
def index():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
