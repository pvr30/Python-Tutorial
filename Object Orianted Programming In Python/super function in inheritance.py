# super() function
"""
Python super function provides us the facility to refer to
the parent class explicitly. It is basically useful where
we have to call superclass functions.
It returns the proxy object that allows us to refer parent class by ‘super’.
"""
class Student:
    def __init__(self, name):
        self.name = name

class Working_Student(Student):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def monthly_salary(self):
        return f"Monthly Salary: {self.salary*30}"

vishal = Working_Student("Vishal Parmar",8000)
print(vishal.name)
print(vishal.salary)
print(vishal.monthly_salary())
