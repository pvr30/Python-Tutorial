# lambda  function.
# Lambda functions are functions that are almost solely used to get inputs and return outputs.
# That means we don't often use them to make actions.
# For example, the `print()` function is a function
# that performs an action. As such, it would not be suitable for lambda function.
# If we wanted a function that just divided two numbers, that might be suitable for a lambda function.
# That's because that function takes inputs, processes them,
# and returns outputs. And, it's a short, simple function
"""def divide(x,y):
    return x/y
print(divide(15,3)) """
# Instead Of This we can use lambda function.

divide = lambda x, y: x/y
print(divide(15, 3))

# or
result = (lambda x, y: x+y)(15, 3)
print(result)



def average(sequences):
    return sum(sequences)/len(sequences)

students = [
    {"name": "Harsh", "grades": (67, 90, 95, 100)},
    {"name": "Manthan", "grades": (56, 78, 80, 90)},
    {"name": "Sahil", "grades": (98, 90, 95, 99)},
    {"name": "Sanjay", "grades": (100, 100, 95, 100)}
]

for student in students:
    print(student["name"], ":")
    print(average(student["grades"]))

# For Above Program We can use lambda function.

print("\n")
average = lambda sequences : sum(sequences)/len(sequences)

students = [
    {"name": "Harsh", "grades": (67, 90, 95, 100)},
    {"name": "Manthan", "grades": (56, 78, 80, 90)},
    {"name": "Sahil", "grades": (98, 90, 95, 99)},
    {"name": "Sanjay", "grades": (100, 100, 95, 100)}
]

for student in students:
    print(student["name"], ":")
    print(average(student["grades"]))


# However you can see that lambda functions can be quite difficult to read,
# so we won't be using them very often. The main reason to use lambda function is because they are short,
# so if we use them in conjunction with other functions
# that can help make our programs a bit more flexible.