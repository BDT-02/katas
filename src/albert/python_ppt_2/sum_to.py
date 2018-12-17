def sum_to(num):
    num = num if num <= 35 else 35
    sum_result = 0
    for i in range(1, num + 1):
        sum_result += i

    return sum_result


val = int(raw_input("Enter value: "))

print("Sum of all integer are: " + str(sum_to(val)))
