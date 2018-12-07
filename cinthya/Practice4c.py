import math
def area_of_circle(r):
    area= math.pi*(r**2)
    print("The area of this circle is: ", area)
def perimeter_of_circle(r):
    area= math.pi*r*2
    print("The perimeter of this circle is: ", area)

r=input("Insert the radius")
area_of_circle(r)
perimeter_of_circle(r)
