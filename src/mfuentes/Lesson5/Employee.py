# Employee will have :
# Employee_Id
# Department
from katas.src.mfuentes.Lesson5.Person import Person


class Employee(Person):
    def __init__(self, name, last_name, age, ci, employee_id, department):
        Person.__init__(self, name, last_name, age, ci)
        self.employee_id = employee_id
        self.department = department

    def get_employee(self):
         return self.employee_id + ", " + self.department


e = Employee('Pepe', 'H', 22, 46556, "3434", "cbba")
print(e.get_employee())
