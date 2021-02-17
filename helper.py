import json


with open("C:\\Users\\user\\PycharmProjects\\Selenium_Python_QA\\users.json") as test_data:
    data = json.load(test_data)
    __admin_login = data["users"][0]["admin_login"]
    __admin_pass = data["users"][0]["admin_pass"]


def get_admin_login():
    return __admin_login


def get_admin_pass():
    return __admin_pass

