import math
def odd_number(x):
    if (x%2==0):
        print ("This is an even number")
    else:
        print ("This is an odd number")

def prime(y):
    count=0
    num=1
    while num<y:
        if ( (y%num) == 0):
            count+=1
        num+=1
    if (count==1):
        print(y, "is a prime number")
    else:
        print(y, "is NOT a prime number")

def numbers(min,max , numbers ):
    for value in numbers:
        if (value>min and value<max ):
            prime(value)

def area_of_circle(r):
    if r>=10:
        area= math.pi*(r**2)
        print("The area of this circle is: ", area)
    else:
        print ("The radius is minor than 10")

def sum_to(n):
    number=1
    sum=0
    while ((number<=n) and (number<=35)):
        sum=sum+number
        number+=1
    print("The sum is ",sum)

def day_in_month(month):
    if (month== "Januar" or month== "March"  or month == "March" or month == "July" or month == "August" or month == "October" or month == "December"):
        print( month, " has ", 31, "days")
    elif (month == "April" or month == "June" or month == "September" or month == "Nobember"):
        print( month, " has ", 30, "days")
    elif (month== "February"):
        print( month, " has ",28, "days")
    else:
        print(month, " is not a valid month")


odd_number(5)
min=5
max=20
n=[1,5,7,8,20,30,6,19]
numbers(min,max,n)
area_of_circle(15)
area_of_circle(7)
sum_to(4)
sum_to(50)
sum_to(0)
day_in_month("December")
day_in_month("Januar")
day_in_month("February")