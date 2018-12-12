#Example1
class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):
    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum
    def GetEmployee(self):
        return self.Name() + ", " + self.staffnumber
x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")
print(x.Name())
print(y.GetEmployee())

#Example2
user_input = input('Type a number:')
try:
#Try do do something that could fail.
    user_input_as_number = float(user_input)
except ValueError:
    # This will be executed if a ``ValueError`` is raised.
    print('You did not enter anumber.')
else:
# This will be executed if not exception got raised inthe
# ``try`` statement.
    print('The square of your number is ',
user_input_as_number**2)
finally:
# This will be executed whether or not an exception israised.
    print('Thank you')