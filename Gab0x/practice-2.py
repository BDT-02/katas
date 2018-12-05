def print_days(age):
    days = age * 365
    return days


def print_hours(age):
    hours = age * 365 * 24
    return hours


def print_minutes(age):
    minutes = age * 365 * 24 * 60
    return minutes


def create_dict():
    users = input("Insert amount of users: ")
    count = 1
    while (count <= users):
        name = raw_input("Insert user name: ")
        age = input("Insert age: ")
        userslist.update({name:age})
        count += 1


def print_user():
    for key, value in userslist.items():
        print key, "=", value
        if (value < 12):
            print "you are a child"
        elif (value >= 13) & (value <= 17):
            print "you are teenager"
        elif (value >= 18) & (value <= 19):
            print "you are young"
        else: print "you are adult"
        print "Age in days: ",print_days(value)
        print "Age in hours: ",print_hours(value)
        print "Age in minutes: ",print_minutes(value)


userslist = {}
create_dict()
print_user()
