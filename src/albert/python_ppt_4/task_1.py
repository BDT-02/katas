def create_dict():
    global items
    num = int(input("How many items doy you want to add the dictionary?: "))
    items = {}
    for i in range(1, num + 1):
        key = raw_input("\nkey for item {}: ".format(i))
        val = raw_input("value for key '{}': ".format(key))
        items[key] = val


def print_keys():
    for key in items:
        print key


def print_values():
    for value in items.values():
        print value


def print_dictionary():
    for key, value in items.items():
        print str(key) + ": " + str(value)


def check_key_exists(k):
    for key in items:
        if key == k:
            return True

    return False


def check_value_exists(v):
    for value in items.values():
        if value == v:
            return True

    return False


# Create dictionary
create_dict()

print "\nLIST OF KEYS:"
print_keys()

print "\nLIST OF VALUES:"
print_values()

print "\nDICTIONARY:"
print_dictionary()

print "\nKEY 'user' exists? : " + str(check_key_exists('user'))

print "\nVALUE 'user' exists? : " + str(check_value_exists('user'))
