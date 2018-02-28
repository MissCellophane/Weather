from flask import render_template, Blueprint


pages = Blueprint('pages', 'pages')


@pages.route('/login_page', methods=['GET', 'POST'])
def login_page():
    return render_template('login.html')


@pages.route('/user_page')
def user_home():
    return render_template('user_page.html')


