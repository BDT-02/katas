dictionary = {}

def dicctionary():
    number=int(input("Insert the lenght of this dictionary"))

    while (len(dictionary)<number):
        key=raw_input("Insert the key value: ")
        content=raw_input("Insert the values: ")
        dictionary[key]=content

def print_values():
    print ("The values are:")
    for value in dictionary:
        print (dictionary[value])

def print_key():
    print ("The key are:")
    for value in dictionary:
        print (value)

def print_dictionary():
    print(dictionary)

def find_key(val):
    if(dictionary.has_key(val)):
        print ("This key value exist into the dictionary")
    else:
        print ("This key value does not exist into the dictionary")

def find_value(val):
    if(val in dictionary.values()):
        print ("This value exist into the dictionary")
    else:
        print ("This value does not exist into the dictionary")


dicctionary()
print_key()
print_values()
print_dictionary()
f_key=raw_input("Insert the key to find")
find_key(f_key)
f_value=raw_input("Insert the value to find")
find_value(f_value)

