
# try , except and finally
"""
number1 = int(input("Enter Number 1:  "))
number2 = int(input("Enter Number 2:  "))
#print(f"The Sum Is {number1 +number2}")

try:
    print(f"The Sum Is {number1 + number2}")
except Exception as e:
    print(e)
"""
class Car:
    def __init__(self, car):
        self.car = car

class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError("You Can Only Make Car Objects ")

        self.cars.append(car)

car_1 = Garage()

swift = Car("SWIFT")
try:
    car_1.add_car(swift)
except TypeError:
    print("Your Car Is Not A Car")
except ValueError:
    print("You Did Something Wrong.")
finally:
    print(swift.car)

"""
There are two benefits:

1. Our code reads more nicely: we try to do something that we expect to be able to do,
   and if we cannot then we say an error happened;
2. Our check for whether it is something we can do is now encapsulated inside 
   the `add_car()` method; we don’t need to have an if statement every time we want to add a car.

The syntax is the `try-catch` syntax.

We try to do whatever is inside the `try` block, and then if an error happens 
we jump to the `except` block. We only do so for errors that match the one in the block
(in this case, `TypeError` would be caught, other errors would not be caught).

We can catch multiple errors (even though our method won’t raise them, just showing you the syntax here):
"""


"""
`try` and `catch` also have a final counterpart: `finally`.

We can use `finally` to run a block of code no matter what happens: 
whether or not an exception is raised. For example:
"""