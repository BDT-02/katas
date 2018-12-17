import math


def area_of_circle(r):
    if r > 10:
        return math.pi * (r**2)
    else:
        return 0


radio = float(raw_input("Radio is: "))

print("Area of circle is: " + str(area_of_circle(radio)))
