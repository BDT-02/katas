def sum_numbers(number):
    sum = 0
    count = 0
    while (count <= number):
        if (count < 35):
            sum = count + sum
        else: break
        count += 1
    return (sum)


number = input("Input a number: ")
result = sum_numbers(number)
print(result)