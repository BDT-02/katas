#Create 1 module to Calculate age in minutes, hours and days

#import math

def calculate_age(age):
    if int(age != 0):
        age_min = age*365*60*24
        age_hour = age*365*24
        age_day = age*365

        print("The age in minutes is: ",age_min )
        print("The age in hours is: ", age_hour)
        print("The age in days is: ", age_day)

#calculate_age(1)
