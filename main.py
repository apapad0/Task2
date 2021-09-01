from login_successful_request import login as test1
from login_erroneous_request import login as test2
from update_user_successfully import update_user_func as test3
from update_user_test_status_code import status as test4
from update_user_test_headers import content_type as test5
from update_user_test_headers import auth as test6
from update_user_test_json import is_json as test7
from update_user_test_json import active as test8
from update_user_test_json import createdAt as test9
from update_user_test_json import createdBy as test10
from update_user_test_json import email as test11
from update_user_test_json import ID as test12
from update_user_test_json import passwordChanged as test13
from update_user_test_json import role as test14
from update_user_test_json import updatedAt as test15
from update_user_test_json import updatedBy as test16

TESTS = [test1, test2, test3]
testAPI1 = [test4, test5, test6]  # status code and headers
testAPI2 = [test7, test8, test9, test10, test11, test12, test13, test14, test15, test16]  # json
fails = []


def test_expected_behaviour():      # successful login, erroneous login, update user
    for test in TESTS:
        if test():
            print('Test', TESTS.index(test) + 1, ': PASS')
        else:
            print('Test', TESTS.index(test) + 1, ': FAIL')
            fails.append(test)


def test_api():
    for test in testAPI1:
        if test():
            print('Test', testAPI1.index(test) + 4, ': PASS')
        else:
            print('Test', testAPI1.index(test) + 4, ': FAIL')
            fails.append(test)
    for test in testAPI2:
        if testAPI2[0]():         # test7git : if the json format is correct it continues, if not it doesn't check its content
            if test():
                print('Test', testAPI2.index(test) + 7, ': PASS')
            else:
                print('Test', testAPI2.index(test) + 7, ': FAIL')
                fails.append(test)
        else:
            print('Test', testAPI2.index(test) + 7, ': FAIL')
            fails.append(test)
            break


if __name__ == "__main__":
    test_expected_behaviour()
    test_api()
    if len(fails) == 0:
        print('SUCCESS')
    else:
        print('Failed tests: ', fails)
