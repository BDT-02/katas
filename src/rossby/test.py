a = 20
b = 100
print a >=b
print a ==b
c = a + b
print c

c -= a
print c

c += a
print c

c /= a
print c


c %= a
print c


a = 7

b = 14

list = [1, 2, 3, 4, 5,7 ];

if ( a in list ):

    print("a exists list")

else:

    print("a does not exist list")

if ( b not in list ):

    print("b does not exist list")

else:

    print("b exists list")



value_1 = 20

value_2 = 30

if ( value_1 is not value_2 ):

    print("Line 1 - a and b have same identity")

else:

    print('Line 1 - a and b do not have same identity')

if ( id(value_1) != id(value_2) ):

    print("Line 2 - a and b have same identity")

else:

    print("Line 2 - a and b do not have same identity")

def newfuction(par1,par2):
    par3 = par1+par2
    print par3
newfuction(2,7)