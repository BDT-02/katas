import datetime
def module1(age):
    if(age<=12):
        print("You are a child")
    elif(age>=13 and age<=17):
        print("You are a teenager")
    elif (age >= 18 and age <= 29):
        print("You are a young")
    if (age >= 30):
        print("You are an adult ")

def module2(birthday):
    now = datetime.datetime.now()
    age_days=((now.year-birthday.year)*365)+((now.month-birthday.month)*30)+now.day-birthday.day
    print (age_days)
    print (now.hour - birthday.hour)
    print (now.minute - birthday.minute)



Age=raw_input("Insert your birthday : ")
a=datetime.datetime.strptime(Age, '%d-%m-%Y %H:%M:%S')
print(a)
module2(a)