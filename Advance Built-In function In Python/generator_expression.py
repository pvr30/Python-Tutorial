numbers_1 = [num for num in [1, 2, 3, 4, 5] ]
print(numbers_1)
# This will give a list

# Generator expression
"""
this is not a tuple of list .
this covert into a generator 
"""

numbers_2 = (num for num in [1, 2, 3, 4, 5])

print(numbers_2)
print(next(numbers_2))
print(next(numbers_2))

for i in numbers_2:
    print(i, end=" ")