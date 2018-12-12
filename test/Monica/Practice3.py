#Function 1:
# - No arguments defined
# - Should ask to the user the number of elements in the list
# - According the value inserted ask for each value of teh array and push it in a new array
# - Return the array

def fill_list():
   num_list = int(input("Number of elements in the list: "))
   lista =[]
   i=0
   if (num_list > 0):
       for i in range(num_list):
           nun=1+1
           val = int(input("Insert value: "))
           lista.append(val)
   return (lista)

lista2 = fill_list()



#Function 2:
# - Should recive 1 argument (the array returned in method 1)
# - Should print the array

def print_list(lista3):
   print(lista3)

print_list(lista2)
