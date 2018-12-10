# Implement the class Person and the subclass employee considering that person will have :
# Name
# Last Name
# Age
# CI
# Employee will have :
# Employee_Id
# Department
# Define both classes into different modules.


class Person(object):
    def __init__(self, name, last_name, age, ci):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.ci = ci

    # def get_name(self):
    #     return self.name
    #
    # def get_last_name(self):
    #     return  self.last_name
    #
    # def get_age(self):
    #     return self.age
    #
    # def get_ci(self):
    #     return self.ci
