def find_key(keyvalue):
    countkey = 0
    for key in dict.keys():
        if (keyvalue == key):
            print keyvalue, " already exist, it is ", key
            countkey = 1
        if (countkey == 1):
            break
    return (countkey)


def find_value(valuevalue):
    countval = 0
    for value in dict.values():
        if (valuevalue == value):
            print valuevalue, " already exist, it is ", value
            countval = 1
        if (countval == 1):
            break
    return (countval)


def create_dict():
    lenDict = input("enter len of the dict: ")
    count = 1
    while (count <= lenDict):
        validatekey = 0
        while (validatekey == 0):
            key1 = raw_input("Enter key :")
            findkey = find_key(key1)
            if (findkey == 1):
                validatekey = 0
            else:
                validatekey = 1
        validatevalue = 0
        while (validatevalue == 0):
            val1 = raw_input("Enter value :")
            findval = find_value(val1)
            if (findval == 1):
                validatevalue = 0
            else:
                validatevalue = 1
        count += 1
        dict.update({key1:val1})

def print_dict():
    print "Dictionary: ",dict

def print_keys():
    print("KEYS:")
    for key in dict.keys():
        print(key)

def print_values():
    print("VALUES:")
    for value in dict.values():
        print(value)

dict = {}
create_dict()
print_dict()
print_keys()
print_values()
for key, value in dict.items():
      print key, "=", value