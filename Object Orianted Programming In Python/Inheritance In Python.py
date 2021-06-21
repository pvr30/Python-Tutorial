#  Inheritance In Python
"""
class First:
    def print_first(self):
        print("Hello First")

class Second(First):  # We Inherit First Class.
    def print_second(self):
        print("Hello Second")

first = Second()
first.print_first()
first.print_second()
"""

"""
class Student:
    def details(self, name, school, marks):
        self.name = name
        self.school = school
        self.marks = marks

    def average_marks(self):
        return f"Average Marks : {sum(self.marks) / len(self.marks)}"

class Working_Student(Student):
    def salaryamount(self,salary):
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}\nSchool Name: {self.school}\nMarks: {self.marks}"


    def weekly_salary(self):
        return f"Monthly Salary: {self.salary*30} "

vishal = Working_Student()
vishal.details("Vishal","Axar",[78,90,36])
print(str(vishal))
vishal.salaryamount(800)
print(vishal.average_marks())
print(vishal.weekly_salary())

harsh = Working_Student()
harsh.salaryamount(9000)

print(harsh.weekly_salary())

"""
# Inheritance for constructor  or super() function

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        return f"Average Marks: {sum(self.marks) // len(self.marks)}"

class Working_Student(Student):
    def __init__(self, name, marks, salary):
        Student.__init__(self,name, marks)
        self.salary = salary

    def monthly_salary(self):
        return f"Monthly Salary : {self.salary*30}"

student_one = Student("Vishal", [78, 90, 80])
print(student_one.average_marks())
student_two = Working_Student("Harsh", [80, 90, 100], 800)
print(student_two.average_marks())
print(student_two.monthly_salary())



