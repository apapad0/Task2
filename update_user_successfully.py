import requests
import json


def login():
    url = "http://localhost:8000/api/v1/authentication/login"

    payload = json.dumps({
        "email": "admin@ekmechanes.com",
        "password": "Password!!!!!"
    })
    headers = {
        'Content-Type': 'application/json',
        'cache-control': 'no-cache'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    token = response.json()['data']['jwt']['accessToken']

    return token


def update_user_func():
    url = "http://localhost:8000/api/v1/users/5ca5ddd23bf77546543e2c9f"

    payload = json.dumps({
        "email": "admin@ekmechanes.com",
        "role": "admin",
        "active": False
    })
    auth = 'Bearer ' + login()          # for the authorization field: 'Bearer token'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response.json()['status'] == "200"


if __name__ == "__main__":
    update_user_func()
