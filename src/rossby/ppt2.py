#example 1
var = 100

if ( var == 100 ) :
    print("Value of expression is %d" % (var))
    print("That is all!!")


#example 2

some_value = 7

if some_value:
    print("Got a true expression value")
    print("Value of expression is %d" % some_value)

else:

    print("Got a false expression value")
    print("Value of expression is %d" % some_value)


#example 3

var = 150
if var == 200:
   print("1 - Got a true expression value")
   print(var)
elif var == 150:
   print("2 - Got a true expression value")
   print(var)
elif var == 100:
   print("3 - Got a true expression value")
   print(var)
else:
   print("4 - Got a false expression value")
   print(var)

print "Good bye!"

#example 3

num = 7
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")


#example 4

count = 0
while (count < 12):
   print("The count is: %d" % count)
   count = count + 1

print("Good bye!")

#example 5

count = 0
while count < 5:
   print (str(count) + " is  less than 5")

         count = count + 1
else:
   print(str(count) + " is not less than 5")



