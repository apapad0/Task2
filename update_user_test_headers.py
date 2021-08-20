from update_user_returns_response import update_user_func as test


def content_type():
    return test().headers['Content-Type'] == 'application/json'


def auth():
    return test().headers['Authorization'][0:6] == 'Bearer'


if __name__ == "__main__":
    content_type()
    auth()
