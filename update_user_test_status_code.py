from update_user_returns_response import update_user_func as test


def status():   # checks if the user is allowed to perform the action
    return test().status_code != 403


if __name__ == "__main__":
    status()
