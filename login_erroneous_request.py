import requests
import json


def login():
    url = "http://localhost:8000/api/v1/authentication/login"

    payload = json.dumps({
        "email": "admin@ekmechanes.com",
        "password": "P4ssword!!!!!"
    })
    headers = {
        'Content-Type': 'application/json',
        'cache-control': 'no-cache'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.json()['error']['messages'])
    return response.json()['status'] == "400"


if __name__ == "__main__":
    login()
