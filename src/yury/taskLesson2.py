import math


def determine_number_odd_or_even(number):
    return "even" if (number % 2 == 0) else "odd"


def determine_number_is_prime(min, max):
    index = min
    prime = []
    while index <= max:
        aux = 2
        is_prime = True
        while aux < index:
            if index % aux == 0:
                is_prime = False
                break
            aux += 1
        if is_prime: prime.append(index)
        index = index + 1
    return prime


def area_of_circle(r):
    result = 0.00
    if r > 10:
        result = math.pi * (r ** 2)
    return round(result, 2)


def sum_to(n):
    sum_total = 0
    if n < 35:
        i = 1
        while i <= n:
            sum_total = sum_total + i
            i += 1
        return sum_total
    return 35


def days_in_month(month):
    months = {'january': 31,
              'february': 28,
              'march': 31,
              'april': 31,
              'may': 31,
              'june': 30,
              'july': 31,
              'august': 31,
              'september': 30,
              'october': 31,
              'november': 30,
              'december': 31,
              }
    month = month.lower()
    return months[month]

