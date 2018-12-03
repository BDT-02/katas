min = input("lower value: ")
max = input("upper value: ")
for number in range(min,max):
    for i in range(2,number):
        if (number % i) == 0:
            break
    else: print(number)