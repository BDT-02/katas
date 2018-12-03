#Write a function area_of_circle(r) which returns the area of a circle of radius r only
# if the radius value is greater of 10.

def area_of_circle(r):
    pi = 3.141592
    if(r > 10):
        r*=r
        area = pi*r
        print("the area is: " + str(area))

radio = int(input("Enter the value for r: "))
area_of_circle(radio)
