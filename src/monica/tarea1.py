
def print_operation(arg1, arg2, ope):
   if (ope == "+"):
        result = arg1 + arg2
   elif (ope == "-"):
        result = arg1 - arg2
   elif (ope == "*"):
        result = arg1 * arg2
   elif (ope == "/"):
        result = arg1 / arg2
   print result
    a = arg1
    b = arg2
    if (a == b):
        print("arg1 is equal to arg2")
    else:
        print("arg1 is different to arg2")
    if (a > b):
        print("arg1 is mayor to arg2")
    print_operation(9,5,"-")

