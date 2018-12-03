var = 100
if (var == 200):
    print("1 - Got a true expression value")
    print(var)
elif (var == 150):
    print("2 - Got a true expression value")
    print(var)
elif (var == 100):
    print("3 - Got a true expression value")
    print(var)
else:
    print("4 - Got a false expression value")
    print(var)

num = -1
if num >= 0:
    if num == 0:
        print ("Zero")
    else:
        print ("Positive number")
else:
    print ("Negative number")


count = 0
while (count < 9):
    print('The count is:', count)
    count = count + 1
print("Good bye!")


count = 0
while count < 5:
    print(count, "is less than 5")
    count = count + 1
else:
    print(count, "is not less than 5")

flag = 0
while (flag):
    print('Given flag is really true!')
print("Good bye!")

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0
# iterate over the list
for val in numbers:
    sum = sum+val
print("The sum is", sum)

