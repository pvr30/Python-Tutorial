# Functions In Python.

def display():  # This is the defining of the function.
    name = input("Enter Your Name: ")
    print(f"Hello , {name}")

display()

# Passing Arguments In Function
# Add Two Numbers.

def add(a,b):
    print(f"The Sum Is {a+b}")

n1 = int(input("Enter a:"))
n2 = int(input("Enter b:"))
add(n1,n2)

# Returning a Value

def maxima(a,b):
    return max(a,b)

print(f"The Maximum Number Is {maxima(n1,n2)}")

# Default Parameters Or Function Overloading.

def sub(a,b=20):
    print(f"The Subtraction Is {a-b}")

sub(n1)
sub(25)

# Error
# We can not make first parameter as a default if we want then we have to make all arguments default
# after first argument .
""" def sub(a=10,b): # We can not do this 
    print(f"The Subtraction Is {a-b}")

sub(n1)
sub(25)  """

default_y = 3

def add(x, y=default_y):
    sum = x + y
    print(sum)


add(2)  # 5

# we can not modify default value once it was define.

default_y = 4
print(default_y)  # 4

add(2)  # 5  