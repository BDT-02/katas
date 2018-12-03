def examples ():
    r=59
    datos = [1, 3, 4, 6, 30, 5, 2]
    print("In example: ", 90 in datos)
    cad1 = ["hoy", "es", "un"]
    cad2 = "es "
    cad3 = "es"
    print("In example: ", cad2 in cad1)
    print("In example: ",cad3 in cad2)
    print("Is example: ",cad3 is cad2)
    if (r>=0):
        print("R es positivo")
    print("R is zero ", r!=0)
def perform_operation(num1,num2,op):
    operations={"+": num1+num2, "*": num1*num2, "/": num1/num2, "%": num1%num2,"**": num1**num2, "//": num1//num2}
    print ("The result is: ", operations[op])

examples()
perform_operation(2,5,"**")
