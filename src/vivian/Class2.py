#PRACTICE 1
#Exercise 1
import math
def number(n):
    if (n%2 == 0):
        print ("Even number")
    else:
        print ("Odd number")
number(10)

#Exercise 2
def prime(a):
    c=0
    n=1
    while n<a:
        if ((a%n) == 0):
            c+=1
        n+=1
    if (c==1):
        print(a, "Prime number")
    else:
        print(a, "Not a prime number")
prime(13)

#Exercise 3
def area_of_circle(r):
    if r>=10:
        a= math.pi*(r**2)
        print("The area of this circle is: ", a)
    else:
        print ("The radius is minor than 10")
area_of_circle(14)

#Exercise 4
def sum_to(n):
    num=1
    sum=0
    while ((num<=n) and (num<=35)):
        sum=sum+num
        num+=1
    print("The sum is ",sum)
sum_to(15)

#Exercise 5
def day_in_month(month):
    if (month== "January" or month== "March"  or month=="May" or month == "July" or month == "August" or month == "October" or month == "December"):
        print( month, " has ", 31, "days")
    elif (month == "April" or month == "June" or month == "September" or month == "November"):
        print( month, " has ", 30, "days")
    elif (month== "February"):
        print( month, " has ",28, "days")
    else:
        print(month, " is not a valid month")
day_in_month("November")
