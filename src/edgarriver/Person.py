#Implement the class Person and the subclass employee considering that person will have :
#Name
#Last Name
#Age
#CI
#Employee will have :
#Employee_Id
#Department
#Define both classes into different modules.

class Person:
    def __init__(self,First_Name, Last_name, Age, CI):
        self.First_Name = First_Name
        self.Last_name = Last_name
        self.Age = Age
        self.CI = CI
    def get_fname(self):
        return self.First_Name
    def get_lname(self):
        return self.Last_name
    def get_age(self):
        return self.Age
    def get_ci(self):
        return self.CI
