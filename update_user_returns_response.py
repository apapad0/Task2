# the purpose of this file is to return the response object, not a true/false condition
import requests
import json

from update_user_successfully import login


def update_user_func():
    url = "http://localhost:8000/api/v1/users/5ca5ddd23bf77546543e2c9f"

    payload = json.dumps({
        "email": "admin@ekmechanes.com",
        "role": "admin",
        "active": False
    })
    auth = 'Bearer ' + login()  # for the authorization field: 'Bearer token'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response


if __name__ == "__main__":
    update_user_func()
