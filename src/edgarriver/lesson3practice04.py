# coding=utf-8
# Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical order
# which occur in the string together with the number of times each letter occurs.
# Case should be ignored. A sample output of the program when the user enters the data
# “ThiS is String with Upper and lower case Letters”, would look this this.
text = raw_input("Enter a text: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_count = {}
for char in text:
    if char in alphabet:
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1
        else:
            letter_count[char] = 1
keys = letter_count.keys()
for key in sorted(keys):
    print(key, letter_count[key])
