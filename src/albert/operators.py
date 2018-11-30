def operation(operator, value1, value2):
    switcher = {
        '+': value1 + value2,
        '-': value1 - value2,
        '*': value1 * value2,
        '/': value1 / value2,
        '%': value1 % value2,
        '**': value1 ** value2,
        '//': value1 // value2
    }

    return switcher.get(operator, 'Invalid operator %s' % operator)


print(operation('+', 5, 2))
print(operation('-', 5, 2))
print(operation('*', 5, 2))
print(operation('/', 5, 2))
print(operation('%', 5, 2))

