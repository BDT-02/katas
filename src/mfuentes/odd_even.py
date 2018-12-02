#1. Create 1 script to determine is a number is odd or even (use single line statement if applies)

def number(num):
    if (num % 2 == 0):
        print( "The number "+ str(num) + " is odd")
    else:
         print( "The number "+ str(num) + " is even")


numero = int(input("Enter a number: "))
number(numero)
