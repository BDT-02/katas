def print_operators(data1, data2, ope):
    if (ope == "+"):
        result = data1 + data2
    elif (ope == "-"):
        result = data1 - data2
    elif (ope == "*"):
        result = data1 * data2
    elif (ope == "/"):
        result = data1 / data2

    print result
    a = data1
    b = data2
    if (a == b):
        print ("data1 equal to data2")
    else:
        print ("data1 is not equal to data2")
    if (a > b):
        print ("data1 is mayor")
    else:
        print ("data1 is not mayor")
print_operators(7, 3, "/")


