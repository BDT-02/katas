
#PRACTICE
# 1. Create 1 script to determine is a number is odd or even (use single line statement if applies)

n = input("Please, set your number:")
if (n%2 == 0):
    print('This number is even')
else:
    print('This number is odd')

# 2. According a list of values between a Min and Max range, identify if the number is prime or not.

number = int(input("Please, enter any number:"))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

else:
    print(number, "is not a prime number")



#EXERCISES

#Write a function area_of_circle(r) which returns the area of a circle of radius r only if the radius value is greater of 10.

import math
def circle_area(r):
    if r>=10:
        b = math.radians(180)
        a = b *(r**2)
        print("The area of the circle with radius:", r, "is", a )
    else:
        print("The radius value is less than 10")

circle_area(77)


#Write a function sum_to(n) that returns the sum of all integer numbers up to and including only until any value lower than 35.
##So sum_to(10)wouldbe1+2+3...+10which would return the value 55, but if n=40 only until sum to 35 need to be returned.


def sum_to(n):
    t = 0
    c = 0
    while(c<=n):
        if (c < 35):
            t += c
            c+= 1
        else:
            break
    print("The sum of the number is:",t)
sum_to(8777)


#Write a function days_in_month which takes the name of a month, and returns the number of days in the month. Ignore leap years:
#		days_in_month("February") == 28 				    days_in_month("December") == 31
#       If the function is given invalid arguments, it should return None.


print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")

import math
def days_in_month(month):
    if month == "February":
        print("No. of days: 28/29 days")
    elif month in ("April", "June", "September", "November"):
        print("No. of days: 30 days")
    elif month in ("January", "March", "May", "July", "August", "October", "December"):
        print("No. of days: 31 day")
    else:
        print("Wrong month name")

days_in_month("June")




