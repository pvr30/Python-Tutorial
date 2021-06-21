"""
Function overloading and Default Argument .
"""

def add(a, b=0):
    return a+b

def add(a, b=0, c=0):
    return a+b+c

print(add(2))
print(add(3, 4))
print(add(3, 4, 5))


# Another example:

friend = {
    'Name': 'Vishal',
    'Age': 19
}

def friend_age(name: str, age: int = 21):    # Default Argument (also write age=21)
    return f"{name} is {age} Years Old"

print(friend_age(friend['Name'], friend['Age']))

