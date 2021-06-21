# for loop

for index in range(10):
    print(index)
print("\n")
for index in range(5,10):
    print(index)
print("\n")
for i in range(1,20,2):
    print(i)  # this will print number between 1 to 20 with difference of 2

# Print list.

name = ["Harsh","Sanjay","Sahil","Manthan"]
for index in name:
    print(index)

# Print list of dictionary .

student_grade = [
    {"name": "Harsh", "grade": 100},
    {"name": "Sahil", "grade": 80},
    {"name": "Manthan", "grade": 10},
]
for student in student_grade:
    name = student["name"]
    grade = student["grade"]
    print(f"{name} got {grade} marks in Exam.")

