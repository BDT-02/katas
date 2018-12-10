# Create 1 script to determine is a number is odd or even
def odd_number(a, b):
    if (a%2==0):
        print ("This is an even number")
    else: ("This is an odd number")
    if (b%2 == 0):
        print ("This is an even number")
    else:
        print ("This is an odd number")
odd_number(6, 13)

# According a list of values between a Min and Max range, identify if the number is prime or not

min = 1
max = 16
print "Prime numbers between",min , "and", max, "are:"

for num in range(min, max + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print (num)

