from flask import Flask, render_template
app = Flask(__name__)
app.secret_key = 'Nothing is wrong!'
from view.login_API import apis
from view.login_pages import pages

app.register_blueprint(apis, url_prefix='/apis')
app.register_blueprint(pages, url_prefix='')


@app.route('/index')
def index():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
