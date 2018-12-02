def get_prime_numbers(min_number,max_number):
    for num in range(min_number, max_number):
        if 0 not in [num % i for i in range(2, int(num / 2) + 1)]:
            print(str(num) + " prime")
        else:
            print(str(num) + " not prime")
get_prime_numbers(int(raw_input("Enter a number: ")), int(raw_input("Enter a number: ")))

