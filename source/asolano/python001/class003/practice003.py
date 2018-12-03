def insert_in_list(number_elements):
    count = 1
    while (count <= number_elements):
        element = raw_input("Insert element : ")
        list.append(element)
        count += 1
    return list

def print_list(list):
    for elements in range(len(list)):
        print(list[elements])


number_elements = input("insert number of elements of the list: ")
list = []
list = insert_in_list(number_elements)
print_list(list)