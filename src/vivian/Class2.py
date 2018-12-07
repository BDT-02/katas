#PRACTICE 1
#Exercise 1
import math
def number(n):
    if (n%2 == 0):
        print ("Even number")
    else:
        print ("Odd number")
number(10)

#Exercise 2
def prime(a):
    c=0
    n=1
    while n<a:
        if ((a%n) == 0):
            c+=1
        n+=1
    if (c==1):
        print(a, "Prime number")
    else:
        print(a, "Not a prime number")

def numb(min,max,numb):
    for value in numb:
        if (value>min and value<max ):
            prime(value)
min=2
max=30
numb(min,max,numb)