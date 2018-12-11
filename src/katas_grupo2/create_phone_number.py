# Exercise:
number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
def create_phone_number(number):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*number)
print create_phone_number(number)


