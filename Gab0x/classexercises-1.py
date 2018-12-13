#A=10
#B=20
a=1
b=2
list=[1,2,3,4,5];

#print A+B
#print A-B
#print A*B
#print A/B

#print A==B
#print A!=B
#print A>B
#print A<B
#print A>=B
#print A<=B

#C = A+B
#print C

#C%=A
#print C

if (a in list):
    print ("a exists list")
else:
    print ("a does not exist list")

value_1=20
value_2=30

if (value_1 is value_2):
    print ("Line 1 - a and b have same identity")
else:
    print ("Line 1 - a and b do not have same identity")

def print_lyrics():
    print("I'm a tester, and I'm okay.")
    print("I sleep all night and I work all day.")
print_lyrics()

def test_part():
    print ("Insert value #1")
    value_a=input()
    print ("Insert value #2")
    value_b=input()
    value_c=value_a*value_b
    print value_c
test_part()