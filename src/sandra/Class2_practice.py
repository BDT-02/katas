num = -1
if num >= 0:
    if num == 0:
        print ("Zero")
    else:
        print ("Positive number")
else:
    print ("Negative number")


count = 0
while (count < 9):
    print('The count is:', count)
    count = count + 1

print("Good bye!")


numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 1
# iterate over the list
for val in numbers:
    sum = sum+val
print("The sum is", sum)



genre = ['pop', 'rock', 'jazz']
#iterate over the list using index
for i in range(len(genre)):
    print ("I like", genre[i])