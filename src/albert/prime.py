def is_prime(number):
    div = number - 1
    prime = True
    while prime and div > 1:
        prime = number % div != 0
        div -= 1

    return prime


range = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for num in range:
    print(num, "is prime" if is_prime(num) else "is not prime")
