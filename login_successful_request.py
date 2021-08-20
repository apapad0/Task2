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
    return response.json()['status'] == "200"


if __name__ == "__main__":
    login()
