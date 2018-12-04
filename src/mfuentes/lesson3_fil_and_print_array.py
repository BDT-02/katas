# Function 1:
# No arguments defined
# Should ask to the user the number of elements in the list
# According the value inserted ask for each value of the array and push it in a new array
# Return the array
def array():
    num = int(input("Enter the number of elements in the list: "))
    array = []
    for k in range(num):
        array.append(input("enter a value"))
    
    print_array(array)

# Function 2
# Should receive 1 argument (the array returned in method 1)
# should print the array

def print_array(ar):
    print (ar)

array()
