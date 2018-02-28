from action.login_check import check, insert_user
from flask import request, jsonify, Blueprint

apis = Blueprint('apis', 'apis')


@apis.route('/login_check', methods=['post', 'get'])
def login_check():
    id = unicode(request.values.get('ID'))
    psw = unicode(request.values.get('PSW'))
    print check(id, psw)
    return jsonify(status=check(id, psw))


@apis.route('/register', methods=['POST', 'GET'])
def register_user():
    id = unicode(request.values.get('ID'))
    psw = unicode(request.values.get('PSW'))
    return jsonify(status=insert_user(id, psw))



