#Create 1 module to Calculate age in minutes, hours and days

age=25 #this is years#
a=25*365 #this is number of days
b=a*24 #this is hours
c=(1*60)*24 #this is the numbers of minutes per day
d=b*c #this is number of minutes

print("If you have")
print (age)
print ("in day are:")
print  (a)
print("in hours are:")
print (b)
print ("and in minutes are:")
print (d)


# Create 1 module to print 4 different messages :
# You are a child, when the age is lower than 12
# Your are teenager, when the age is between 13 and 17
# You are young, when the age is between 18 and 29
# You are adult, when the age is greater than 30


age = 0
while (age <=31):

  # print('The count is:', age)
   age = age + 1
   if age==12:
       print("you were a child")
   elif age>=13 and age<=17:
       print ("you were a teenager")
   elif age>=18 and age<=29:
       print("you were a young")
   elif age==30:
       print("you're an adult")
   else:
       print("you are major than 30")

print("Good bye, have a good day!")


# Create a script importing both modules and performing de action :
# Ask to the user the amount of users
# For all users define the name and the age for each one, save this data as a dictionary
# After all users are defined, need to :
# print the age in minutes, hours and days
# The expected message according the age define

users=15
