class Person:
    def __init__(self, first, last, age, ci):
        self.firstname = first
        self.lastname = last
        self.personage = age
        self.personci = ci

    def Name(self):
        return self.firstname + "" + self.lastname + "" + self.personage + "" + self.personci


class Employee(Person):
    def __init__(self, first, last, age, ci, id, dep):
        Person.__init__(self, first, last, age, ci)
        self.employeeid = id
        self.department = dep
    def GetEmployee(self):
        return self.Name() + "," + self.employeeid + "," + self.department

x = Person("Sandra", " Rada", " 27", " 123456")
y = Employee("Jonas", " Aramayo", " 32", " 789654", " 1234", " RH")

print(x.Name())
print(y.GetEmployee())
