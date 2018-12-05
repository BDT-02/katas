import re

def isValidEmail(email):
        if len(email) > 7:
            if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
                return True
        return False


def ask_password():
    password = raw_input("Insert password: ")
    len2 = len(password)
    if ((len2 >= 8) & (len2 <= 16)):
        pass
    else:
        return 1
    validatepassword = 0
    countlower = 0
    countupper = 0
    countnumber = 0
    for c in password:
        if (((c >= 'a' ) & (c <= 'z' )) | ((c >= '0' ) & (c <= '9' )) | ((c >= 'A' ) & (c <= 'Z' ))):
            if ((c >= 'a' ) & (c <= 'z' )):
                countlower = 1
            elif ((c >= 'A' ) & (c <= 'Z' )):
                countupper = 1
            elif ((c >= '0' ) & (c <= '9' )):
                countnumber = 1
        else:
            validatepassword = 1
    if (validatepassword | (countlower == 0) | (countupper == 0) | (countnumber == 0)):
        validatepassword = 1
        print "Invalid password"
    return (validatepassword)


def ask_username():
    username = raw_input("Insert user name: ")
    username = username.lower()
    len1 = len(username)
    validateuser = 0
    for c in username:
        if (((c >= 'a' ) & (c <= 'z' )) | ((c >= '0' ) & (c <= '9' )) | (c == '_')):
            pass
        else:
            validateuser = 1
    if (validateuser):
        print "Invalid username"
    return (validateuser)


validate1 = 1
while (validate1 == 1):
    validate1 = ask_username()

validate2 = 1
while (validate2 == 1):
    validate2 = ask_password()

