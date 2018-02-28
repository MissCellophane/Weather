from pymongo import MongoClient

client = MongoClient()
db = client.weatherDB
users = db.User


def insert_user(uid, password):
    user = users.find_one({'uid': uid})
    if user:
        return 1
    users.insert({'uid': uid,
                  'password': password})
    return 0


def check(uid, password):
    user = users.find_one({'uid': uid})
    if not user:
        return 0
    print password, type(password)
    print user.get('password'), type(user.get('password'))
    return 1 if password == user.get('password') else 0


