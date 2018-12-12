
#PRACTICE
#1
# Suppose any line of text can contain at most one url that starts with =http://= and ends at the
#       next space in the line. Write a fragment of code to extract and print the full url if it is present.

# Using the regular expression

import re

def Find(string):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ])+', string)
    return url
string = 'https://github.com this is a test http://www.jalasoft.com'
print("Urls: ", Find(string))


#2
#Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s:


del replace("word", "a", "b")


    replace("Mississippi", "i", "I") # == "MIssIssIppI"
    song = "I love spom! Spom is my favorite food.Spom, spom, yum!"

replace("Mississippi", "i", "I") # == "MIssIssIppI"
replace(s, "om", "am") # == "I love spam! Spam is my favorite food. Spam,spam, yum!"
replace(s, "o", "a") #== "I lave spam! Spam is my favarite faad. Spam,spam, yum!"


#3
#Function 1:
#No arguments defined
#Should ask to the user the number of elements in the list
#According the value inserted ask for each value of the array and push it in a new array
#Return the array
#Function 2
#Should receive 1 argument (the array returned in method 1)
#should print the array

#4

#Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical
#    order which occur in the string together with the number of times each letter occurs.
#    Case should be ignored. A sample output of the program when the user enters the data
#    =ThiS is String with upper and lower case Letters=, would look this this =>

#a 2
#c 1
#d 1
#e 5
#g 1
#h 2
#i 4
#l 2
#n 2
#o 1
#p 2
#r 4
#s 5
#t 5
#u 1
#w 2

###RESEARCH

#Python Dictionary built-in functions.
#Modules
#What is a module
#Most common built in modules
#How to define custom modules
#Packages
#How to declare them
#Benefits of using packages
#Regular expressions
#Patterns
#Modifiers




num = -1
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")


count = 0
while (count < 9):
   print('The count is:', count)
   count = count + 1

print("Good bye!")


numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0
# iterate over the list
for val in numbers:
   sum = sum+val
print("The sum is", sum)
