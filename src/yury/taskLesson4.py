def create_dictionary():
    global dictionary
    dictionary = {}
    size = input()
    i = 0
    while i < size:
        key = raw_input()
        value = raw_input()
        dictionary[key] = value
        i += 1
    return dictionary


def show_keys_dictionary():
    print dictionary.keys()


def show_values_dictionary():
    print dictionary.values()


def show_dictionary():
    print dictionary


def add_key_dictionary():
    keys = dictionary.keys()
    new_key = raw_input("insert the new key")
    if new_key in keys:
        print "the key already exist"
    else:
        print "the new key added"


def add_value_dictionary():
    values = dictionary.values()
    new_value = raw_input("insert the new value1")
    if new_value in values:
        print "the value already exist"
    else:
        print "the new value was add"
