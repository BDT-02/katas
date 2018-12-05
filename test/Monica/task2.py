#1. Create 1 script to determine is a number is odd or even (use single line statement if applies)
num = 9
if (num%2 == 0): print ("The number: ",num," is odd")
else: print ("The number: ",num," is even")

#2. According a list of values between a Min and Max range, identify if the number is prime or not.
min = 1
max = 20
lista= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
i=0
for min in range(max):
    lista[i] = min
    i=+i


def primos(n):
    "Función que calcula los números primos hasta n"
    for i in range(2, n):
        for x in range(2, i):
            if i % x == 0:
                # print i, '=', x, 'por', n/x
                break  # No se ejecuta el else

        else:
            print
            i, 'es primo.'