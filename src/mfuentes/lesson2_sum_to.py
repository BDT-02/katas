#Write a function sum_to(n) that returns the sum of all integer numbers up to
# and including only until any value lower than 35. So sum_to(10)wouldbe1+2+3...+10
# which would return the value 55, but if n=40 only until sum to 35 need to be returned.

def sum_to(n):
    sum = 0
    if(n >= 35):
        for i in range(1,35):
            sum += i
    else:
        for i in range(1,n+1):
            sum += i
    print("The num is:" + str(n)+ " and the sum is: " + str(sum))


numero = int(input("Enter a number: "))
sum_to(numero)
