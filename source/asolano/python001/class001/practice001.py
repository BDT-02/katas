a = 10
b = 20
operator = "*"

def operation(a,b,operator):
    if (operator=="*"):
        print(a,"*",b,"=",a*b)
    elif (operator=="+"):
        print(a,"+",b,"=",a+b)
    elif (operator=="-"):
        print(a,"-",b,"=",a-b)
    elif (operator=="/"):
        if (a>b):
            print(a,"/",b,"=",a/b)
        else:
            print(b,"/",a,"=",b/a)

operation(a,b,"+")
operation(a,b,"-")
operation(a,b,"*")
operation(a,b,"/")