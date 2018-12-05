def ask_number():
    validateInput = 1
    while (validateInput == 1):
        number = raw_input("Insert one digit: ")
        if number not in {'1', '2', '3','4','5','6','7','8','9'}:
            print "Insert only one digit"
            validateInput = 1
        else: validateInput = 0
    print number

def usename_request():
    countU = 1
    while (countU == 1):
        username1 = raw_input("Insert username: ")
        len1 = len(username1)
        if (len1 > 8):
            countU == 1
        else:
            countU == 0
        for (c in username1):
            if (c <= 'a' & c => 'z'):
                countU = 1


def create_list():
    users = input("Insert amount of users: ")
    count = 1
    while (count <= users):
        username1 = raw_input("Insert username: ")

        userid = input("Insert userId: ")
        if (userid  in range(0,100)):
            print "valid"
        else: print "invalid"
        userslist.update({username1:userid})
        count += 1


userslist = {}
create_list()
ask_number()



