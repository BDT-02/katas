#Take an array and remove every second element out of that array. Always keep the first element and start removing with the next element.
#Example:
#my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...]
#None of the arrays will be empty, so you don't have to worry about that!

def removesecond ():
    lista = ['a','b','c','d','e','f','g','1','2','3','4','5','6']
    tamlista= len(lista)
    n=0
    while (n < tamlista):
        print (lista[n])
        n = n+2
removesecond()