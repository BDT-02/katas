# Create a script importing both modules and performing de action :
# Ask to the user the amount of users
# For all users define the name and the age for each one, save this data as a dictionary
# After all users are defined, need to :
# print the age in minutes, hours and days
# The expected message according the age define


import calculate_age
import person_age


def users1(num):
    usuarios = {}
    nu = int(num)
    i = 0
    while i < nu:
        nombre = str(input("Enter your name: "))
        edad = int(input("Enter your age: "))
        usuarios[nombre] = edad
        calculate_age.calculate_age(edad)
        person_age.person_age(edad)
        i = i =1


n = int(input("Enter the number of users:"))
users1(n)
