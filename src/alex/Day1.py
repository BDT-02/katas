a= 2
b= 3

suma = a + b
print(suma)

suma = a * b
print(suma)

suma = a / b
print(suma)

suma = a % b
print(suma)

print a**b

print a==b

print a!=b

print a>b

print a>=b

print a<b

print a<=b


a='hello'
b='world'
list=['hello','world','canta','eassy','hard'];
if ('hello' in list):
    print('hello exist in the list')
else:
    print('hello doesnt exist in the list')

if ('llora' not in list):
    print('llora doens exist in the list')
else:
    print('llora exist in the list')


def print_lyrics():
    print("I'm a tester, and I'm okay.")
    print("I sleep all night and I work all day.")
print_lyrics()


value_1 = 20
value_2 = 20

if ( value_1 is value_2 ):
   print("Line 1 - a and b have same identity")
else:
   print('Line 1 - a and b do not have same identity')

if ( id(value_1) == id(value_2) ):
   print("Line 2 - a and b have same identity")
else:
   print("Line 2 - a and b do not have same identity")
