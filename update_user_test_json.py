from update_user_returns_response import update_user_func as test
import json


def is_json():
    try:
        json.loads(test().json())
        return True
    except:
        return False


def active():
    return type(test().json()['data']['user']['active']) == bool


def createdAt():
    return type(test().json()['data']['user']['createdAt']) == str


def createdBy():
    return type(test().json()['data']['user']['createdBy']) == str


def email():
    return type(test().json()['data']['user']['email']) == str


def ID():
    return type(test().json()['data']['user']['id']) == str


def passwordChanged():
    return type(test().json()['data']['user']['createdBy']) == bool


def role():  # checking valid values for role
    return type(test().json()['data']['user']['role']) == str


def updatedAt():
    return type(test().json()['data']['user']['updatedAt']) == str


def updatedBy():
    return type(test().json()['data']['user']['updatedBy']) == str


def status():
    return type(test().json()['status']) == str


if __name__ == "__main__":
    if is_json():
        active()
        role()
        createdAt()
        createdBy()
        email()
        ID()
        passwordChanged()
        role()
        updatedAt()
        updatedBy()
        status()
    else:
        print('Not a json.')
