#Create a script to ask to the user of the radio and print both results.

import area
import perimeter


def circle(r):

    # if type(r)!=type("a"):
    #     print("El radio tiene que ser un numero")
    # else:
    if r >= 0:
        area1 = float(area.area_circle(r))
        peri = float(perimeter.perimeter_circle(r))
        print("The area of the circle is: ", area1)
        print("The perimeter of the circle is: ", peri)

    else:
        print("Invalid data was entered")

radius = float(input("Enter the radius of the circle: " ))
circle(radius)
