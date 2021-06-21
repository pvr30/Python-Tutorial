class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student("Vishal",[50,45,90,80,75])
student_two = Student("Harsh",[80,96,98,100,63])
print(Student.average(student_one))
print(student_two.grades)
print(student_two.average())