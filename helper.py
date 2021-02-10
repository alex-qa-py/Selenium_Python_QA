import json


with open("users.json") as user:
    data = json.load(user)
    __admin_login = data["users"][0]["admin_login"]
    __admin_pass = data["users"][0]["admin_pass"]


def get_admin_login():
    return __admin_login


def get_admin_pass():
    return __admin_pass

