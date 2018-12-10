from src.edgarriver.Person import Person

class Employee(Person):
    def __init__(self, employee_ID, Depto):
        self.employee_ID = employee_ID
        self.Depto = Depto
edgar = Person('edgar', 'quispe', '38', '3731335cba')
edgar1 = Employee('emp01', 'QA')
print edgar.get_lname()+' '+edgar.get_fname()+' '+edgar1.Depto