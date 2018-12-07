class Person:
    def __init__(self, first, last, age, ci):
        self.firstname = first
        self.lastname = last
        self.agename = age
        self.ciname = ci
    def Name(self):
        return self.firstname + " " + self.lastname + " " + self.agename + " " + self.ciname

class Employee(Person):
    def __init__(self, first, last, age, ci, id, department):
        Person.__init__(self,first, last, age, ci)
        self.idemployee = id
        self.departmentemployee = department
    def GetEmployee(self):
        return self.Name() + ", " + self.idemployee + ", " + self.departmentemployee

x = Person("Marge", "Simpson","20", "12345")
y = Employee("Homer", "Simpson", "15", "234567", "1007", "HR")

print(x.Name())
print(y.GetEmployee())

def __init__(self, first, last, age, ci, id, department):
    super().__init__(first, last, age, ci)
    self.idemployee = id
    self.departmentemployee = department