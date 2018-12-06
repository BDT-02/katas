#1. Create 1 script to determine is a number is odd or even (use single line statement if applies)
print ("practice 1")
num = 9
if (num%2 == 0): print ("The number: ",num," is odd")
else: print ("The number: ",num," is even")

#2. According a list of values between a Min and Max range, identify if the number is prime or not.
def es_primo(n: object) -> object:
    a=0
    for i in range(1, n + 1):
        if (n % i == 0):
            a = a + 1
    if (a != 2):
        print(n,"No es primo")
    else:
        print(n,"si es primo")
#es_primo(3)

def llenarlista(min,max):
    lista = []
    i=0
    #lista.insert(i,min)
    max3=max-min
    for i in range(max3+1):
        lista.insert(i,min+i)
    return lista
print ("practice 2")
min2=40
max2=50
listallena = llenarlista(min2,max2)
i=0
j= max2-min2+1
for i in range(j):
    val=listallena[i]
    es_primo(val)
