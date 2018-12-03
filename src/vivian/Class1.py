#Class 1
#Practice 1
def perform_operation(n1,n2,op):
    operations={"+": n1+n2, "*": n1*n2, "/": n1/n2, "%": n1%n2,"**": n1**n2, "//": n1//n2}
    print ("The result is: ", operations[op])
perform_operation(2,5,"**")


#Practice 2
a=20
b=2
c=10

#Arithmetic's operators
print a+b
print a-b
print a*b
print a/b
print a**b
print a//b

#Comparison operators
print a>b
print a!=b
print a==b
print b<a
print a>=b
print b<=a

#Assignment operators
c+=a
print c
c-=a
print c
c*=a
print c
c/=a
print c
c%=a
print c
