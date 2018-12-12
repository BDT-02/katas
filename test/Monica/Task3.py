#Write a program that reads a string and returns a table of the letters of the alphabet in
# alphabetical order which occur in the string together with the number of times each
# letter occurs.
# - Case should be ignored. A sample output of the program when the user enters the data
# "ThiS is String with Upper and lower case Letters".

entrada = input("Introduce una cadena: ")

diccionario = {}
for letra in entrada:
   if letra in diccionario:
       diccionario[letra] = diccionario[letra] + 1
   else:
       diccionario[letra] = 1

for k, v in diccionario.items():
  if (k!=" "):
       print ("%s: %s" % (k, v))


#Suppose any line of text can contain at most one url that start with "http://" and
#ends at the next space in the line. Write  a fragment of code to extract and print
#the full url if it si present

texto = "this is an example of the strig manage, this is the url http://www.google.com/ that will be displayed"
lista_texto = texto.split()
tamlista= len(lista_texto)
#print (tamlista)
url1 = "http://"
x=0
url2="x"
for x in range(tamlista):
   pal= lista_texto[x]
   #print (pal)
   if (url1 in pal):
       url2= pal
if (url2 == "x"):
   print ("Doen't exist the url")
else:
   print("The url is: ", url2)


#Write a function replace (s,old, new) that replaces all occurrences of old with new in a string s

def replace(s,old, new):
  new_word = s.replace(old, new)
  return new_word

word1= replace("Mississippi","i","I")
print( "Output of replaced is: ", word1)
song ="I love spom! Spom is my favorite food.Spom spom, yum!"
word1= replace(song,"om","am")
print( "Output of replaced is: ", word1)
old1="o"
new1="a"
word1= replace(song,old1,new1)
print( "Output of replaced is: ", word1)
