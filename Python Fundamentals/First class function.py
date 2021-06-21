# First Class Functions
# A Function which can you pass to another function as a argument.
# All functions in Python are just variables,
# which means you can pass them to other functions as arguments.
def greet():
    print("Hello")
greet()
hello = greet  # We can assign one function into another function name.
hello()

average = lambda seq: sum(seq)/len(seq)
total = lambda seq: sum(seq)
maximum = lambda seq: max(seq)

choice = {
    "Average": average,  # This makes choices easy.
    "Total": total,
    "Maximum": maximum
}
students_info = [
    {"name": "Harsh", "grades": (67, 90, 95, 100)},
    {"name": "Manthan", "grades": (56, 78, 80, 90)},
    {"name": "Sahil", "grades": (98, 90, 95, 99)},
    {"name": "Sanjay", "grades": (100, 100, 95, 100)}
]

for student in students_info:
    name = student["name"]
    grades = student["grades"]
    print(f"Student: {name}")
    user_choice = input("Enter Average , Total and Maximum anything you Want :")
    operation_choice = choice[user_choice]
    print(operation_choice(grades))

