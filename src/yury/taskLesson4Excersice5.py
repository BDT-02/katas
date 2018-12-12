import re


def set_user_name():
    print "insert name with lowercase letter (a-z), number (0-9), an underscore"
    user_name = raw_input()
    regular_expression = re.match('^[a-z0-9_]*', user_name)
    if regular_expression:
        print "user name added"
    else:
        print("only write letter (a-z), number (0-9), an underscore")


def set_password():
    print "insert name with lowercase letter (a-z), number (0-9), an underscore"
    # regular_expression = re.match('^[(a-z0-9\_\-\.)]{2,15}$', "yury_yver*/AB_789")
    user_name = raw_input()
    regular_expression = re.match('^[a-z0-9A-Z]{7,16}$', user_name)
    if regular_expression:
        print "password added"
    else:
        print(
            "only writeletter (a-z), number (0-9), letter (A-Z) and the length have to be between 8 and 16 characters")


