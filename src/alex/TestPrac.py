a = ['banana', 'apple', 'Microsoft']
print[a]
print(a[2])
print a[1]
print a[0]
print a[-1]

b = ['ball', 'socks', 'tshirt']
for fruits in b:
    print (fruits)
    print (fruits)

c = [20, 214, 11]
total = 0
for n in c:
    total = total + n
print(total)

d = list(range(2, 30))
print(d)

total2 = 0
for i in range(2, 30):
    total2 += i
print(total2)

total3 = 0
for i in range(1, 8):
    if i % 3 == 0:
        total3 += i
print(total3)

total4 = 0
for i in range(1, 100):
    if i%3 == 0 or i%5 == 0:
        total4 += i
print(total4)
