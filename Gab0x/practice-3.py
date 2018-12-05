def print_area(radio,pi):
    area = radio * 2 * pi
    return area

def print_perimeter(radio,pi):
    perimeter = radio * radio * pi
    return perimeter

PI = 3.14
radio = input("Insert radio: ")
print "AREA: ",print_area(radio,PI)
print "PERIMETER: ",print_perimeter(radio,PI)