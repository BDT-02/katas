#1. Write a function area_of_circle(r) which returns the area of a circle of radius r only if the radius
# value is greater of 10.
print ("Exercise 1:")
def area_radio(r):
    pi = 3.1416
    area = r**2*pi
    if (area > 10):
        print ("El area es: ",area)
    else:
        print ("El area es menor que 10")

area_radio(10)

#2. Write a function sum_to(n) that returns the sum of all integer numbers up to and including only until any
# value lower than 35. So sum_to(10)wouldbe1+2+3...+10which would return the value 55, but if n=40 only until
# sum to 35 need to be returned.
print ("Exercise 2:")
def sum_to(n):
    suma=0
    i = 1
    if (n <= 35):
        for i in range(n+1):
            suma+=i
            #print(suma)
    else:
        for i in range(36):
            suma+=i
            #print(suma)
    print ("la suma es:", suma)
    #print (i)
sum_to (80)
# 3. Write a function days_in_month which takes
# the name of a month, and returns the number
# of days in the month. Ignore leap years:
#
# days_in_month("February") == 28
# days_in_month("December") == 31
#
# If the function is given invalid arguments, it
# should return None.
print ("Exercise 3:")
def days_in_month(month):
    if ((month == "January") or (month == "March") or (month == "May") or (month == "July") or (month == "August") or (month == "October") or (month == "December")):
        dias=31
    elif ((month == "April") or (month == "June") or (month == "September") or (month == "November ")):
        dias=30
    elif (month == "February"):
        dias=28
    print (month, "month have", dias , "days")
days_in_month("September")
