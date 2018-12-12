import random
import string


def create_users():
    global users
    users = {}
    for i in range(1, 101):
        users[i] = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))


def get_user_ids_by_number(num):
    ids = []
    for id in users:
        if str(id).startswith(str(num)):
            ids.append(id)
    return ids
