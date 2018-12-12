# local variables
sz = 2
def h2():
   global sz
   #tess.turn(42)
   #tess.forward(sz)
   sz += 1
h2()
print (sz)

song = "The rain in Spain..."
words= song.split()
print (words)
words= song.split("ai")
print (words)

song = "The rain in Spain..."
words= song.split()
glue=";"
phrase= glue.join(words)
print (phrase)

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'John','code':6789,'dept':'sales'}
print (dict['one'])
print (dict[2])
print (tinydict)
print (tinydict.keys())
print (tinydict.values())
