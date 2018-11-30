def sum_to(num):
    num = num if num <= 35 else 35
    sum_result = 0
    for i in range(1, num + 1):
        sum_result += i

    return sum_result


val = int(input("Enter value: "))

print("Sum of all integer are: ", sum_to(val))
