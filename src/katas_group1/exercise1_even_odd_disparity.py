def solve(a):
    countE=0
    countO=0    
    for value in a:
        if(type(value) is int):
            if (value%2==0 or value==0):
                countE+=1
            elif(value%2==1):
                countO+=1
    return(countE-countO)
