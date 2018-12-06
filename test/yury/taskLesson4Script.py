from src.yury.taskLesson4Convertions import convert_age_to_minutes, convert_minutes_to_day, convert_minutes_to_hour
from src.yury.taskLesson4ShowMessage import show_message_1, show_message_2, show_message_3, show_message_4

users = {}
number_user = input("enter the number user: ")

i = 0
while i < number_user:
    name = raw_input("enter name user: ")
    age = raw_input("enter the age user: ")
    users[name] = age
    i += 1

for name, age in users.items():
    age = int(age)
    print "Age in minutes: " + str(convert_age_to_minutes(age))
    print "Age in days: " + str(convert_minutes_to_day(age))
    print "Age in hour: " + str(convert_minutes_to_hour(age))
    if age <= 12:
        show_message_1()
    elif 13 <= age <= 17:
        show_message_2()
    elif 18 <= age <= 29:
        show_message_3()
    else:
        show_message_4()
