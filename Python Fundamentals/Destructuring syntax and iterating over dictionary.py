# Destructuring syntax
number = 1,2,3  # this is a tuple we can define it without brackets
print(number)
for i in number:
    print(i)

# Destructuring a list.
friends_age = [("Harsh",25),("Sahil",20),("Manthan",45)]
for name,age in friends_age:
    print(f"{name} is {age} years Old.")


# Iterating Over Dictionary.

friends_marks = {"Harsh":100,"Manthan":50,"Sahil":70}
for name in friends_marks:
    print(name)

for marks in friends_marks.values():
    print(marks)


for name,marks in friends_marks.items():
    print(name,marks)

for name,marks in friends_marks.items():
    print(f"{name} got {marks} marks in Exam.")