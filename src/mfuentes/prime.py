#2. According a list of values between a Min and Max range, identify if the number is prime or not.

def prime(min, max):
     for num in range(min,max):
        if 0 not in [num%i for i in range(2,int(num/2)+1)]:
            print( str(num) + " prime")
        else:
            print( str(num) + " not prime")


min = int(input("Enter the min value: "))
max = int(input("Enter the max value: "))
prime(min,max)
