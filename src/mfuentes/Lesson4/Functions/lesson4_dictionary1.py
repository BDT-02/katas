# 1.Function to create the dictionary, the Function should ask for the length of the dictionary
# According the length defined should ask to the user for the key and for the value.

def dicci():
    num = int(input("Enter the number of elements in the list: "))

    dic = {}
    i = 0
    while i < num:

        key = input("Enter the key to be added:")
        value = input("Enter the value for the key to be added:")

        dic.update({key:value})
        i = i + 1
    print(dic)
    print_dictionary_keys(dic)
    print_dictionary_values(dic)
    key_exist(dic)
    value_exist(dic)
    dic.keys()

#2. Function to print the dictionary keys

def print_dictionary_keys(dic):
    #print(dic.keys)
    for key in dic:
        print("the key name is: " + key)
    print("----------------------")

#3. Function to print the dictionary values
def print_dictionary_values(dic):
    #print(dic.keys)
    for key in dic:
        print("the value is: " + dic[key])
#4. Function to print the dictionary
def print_dictionary(dic):
    print(dic)

#5. Function to define is a key inserted by the user, exists on the dictionary.

def key_exist(dic):
    key = input("Enter the key to see if exists:")
    if key in dic:
        print("Yes, " + key + " key exists in dict")
    else:
        print("No," + key + " key does not exists in dict")

#6. Function to define is a value inserted by the user, exists on the dictionary.

def value_exist(dic):
    value = input("Enter the value to see if exists:")

    for key in dic:
        if value == dic[key]:
            print("Yes, " + value + " value exists in dict")
            break
        else:
            print("No, " + value + " value does not exists in dict")


#7. Use the dictionary as a Global variable to be used in all fucntions.

dicci()
