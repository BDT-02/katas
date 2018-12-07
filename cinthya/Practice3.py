urls="http://www.google.com  Hola Mundo http://www.facebook.com http://www.gmail.com "
sentence="Hello this is a test for a replace function"
message1 = []

def find_Url():
    print (len(urls))
    url=urls.split(" ")
    for value in url:
        if ("http://" in value):
            print (value)

def replaceLet(v, o, n):
    sentence=v.replace(o, n)
    print (sentence)

def function1():
    number = int(input("Write the number of values to read"))
    print(number)
    while (len(message1) < number):
        message1.append(input("Insert a new numeral value: "))
    print (message1)

def function2():
    print("FUNCTION 2")
    print (message1)

def count_letters():
    example= raw_input("Introduce a sentence")
    letters = {}
    for character in example.lower():
        if (letters.has_key(character) and character!=" "):
            letters[character] = letters[character] + 1
        elif character!=" ":
            letters[character] = 1
    sorted(letters,key=str)
    print(letters)


print("URL FUNCTION ")
find_Url()
print("REPLACE FUNCTION ")
replaceLet(sentence,"i", "A")
print("FUNCTION 1")
function1()
function2()
count_letters()
