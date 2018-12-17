from task_2 import age as usr_age
from task_2 import message

num = int(input("Number of users: "))

users = {}
for n in range(1, num + 1):
    name = raw_input("Name user {}: ".format(n))
    age = int(input("Age of {}: ".format(name)))
    users[name] = age

for name, age in users.items():
    print "\n" + str(name) + " is " + str(age) + " years old. In days, hours and minutes is:"
    print "Days: " + str(usr_age.days(age))
    print "Hours: " + str(usr_age.hours(age))
    print "Minutes: " + str(usr_age.minutes(age))
    message.msg(age)
