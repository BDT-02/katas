def circle_area(radio):
    if (radio >= 10):
        PI = 3.14
        area1 = PI * radio * radio
        return(area1)
    else: print("radio is lower than 10")


radio = input("enter the radius of a circle: ")
result = circle_area(radio)
print(result)