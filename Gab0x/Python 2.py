#var = input()
#if ( var == 100 ):
#   print("Value of expression is %d" % (var))
#   print("That is all!!")


#some_value = 1
#if some_value:
#    print("Got a true expression value")
#   print(some_value)
#else:
#   print("Got a false expression value")
#   print(some_value)



#var = 200
#if var == 200:
#    print("1 - Got a true expression value")
#   print(var)
#elif var == 150:
#    print("2 - Got a true expression value")
#    print(var)
#elif var == 100:
#    print("3 - Got a true expression value")
#    print(var)
#else:
#    print("4 - Got a false expression value")
#    print(var)

#num = -1
#if num >= 0:
#   if num == 0:
#       print("Zero")
#   else:
#       print("Positive number")
#else:
#   print("Negative number")

count = 0
while (count <= 9):
    print("The count is = %d" % count)
    count = count + 1

print("Good bye!")


counts = 0
while counts < 5:
    print("%d is less than 5" % counts)
    counts = counts + 1
else:
    print(str(counts) + " is not less than 5")

flag = 0
while (flag):
    print('Given flag is really true!')
print("Good bye!")


genre = ['pop', 'rock', 'jazz']
# iterate over the list using index
for i in range(len(genre)):
    print("I like %s" % genre[i])