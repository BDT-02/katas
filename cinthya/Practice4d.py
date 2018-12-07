users = {}
def add_user():
    userID = input("Insert the userId value: ")
    if (userID>=1 and userID<=100):
        errorID=False;
    else:
        print("The userID is not valid ")
        errorID=True;
    userName = raw_input("Insert the userName values: ")
    if(len(userName)<=8 and userName.lower()):
        errorNAME=False
    else:
        print("The userName is not valid. It should content at most 8 characters ")
        errorNAME=True
    if(errorID==False and errorNAME==False):
        users[userID] = userName

def find_userId(number):
    count=0
    for value in (users.keys()):
        if (str(number) in str(value)):
           count+=1

    print("The number of users are: ", count)
def find_userName(nam):
    count=0
    for val in (users.values()):
        if (nam in val):
           count+=1

    print("The number of users are: ", count)
def clasify_users(userdI):
    if(userdI>=1 and userdI<=25):
        print ("User belong Group 1")
    elif(userdI>=26 and userdI<=50):
        print ("User belong Group 2")
    elif(userdI>=51 and userdI<=75):
        print ("User belong Group 3")
    elif (userdI >= 76 and userdI <= 100):
        print ("User belong Group 4")
def print_dic():
    print(users)

number_dic=input("Insert the number of users: ")
while(len(users) <number_dic):
    add_user()
num=input("1. Insert a number to find: ")
find_userId(num)
name=raw_input("2. Insert a name to find: ")
find_userName(name)
print("CLASSIFY USERS: ")
for value in users.keys():
    clasify_users(value)