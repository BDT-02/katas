import random


def random_name():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    name = ""
    for num in range(8):
        i = random.randint(0, len(alphabet))
        name += alphabet[i]

    return name


def create_users():
    global users
    users = {}
    for i in range(1, 101):
        users[i] = random_name()


def get_user_ids_by_number(num):
    ids = []
    for id in users:
        if str(id).startswith(str(num)):
            ids.append(id)

    return ids


def get_user_name_by_char(char):
    names = []
    for name in users.values():
        if str(name).startswith(str(char)):
            names.append(name)

    return names
