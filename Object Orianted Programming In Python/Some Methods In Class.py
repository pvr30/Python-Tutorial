# Some Useful Method("Dunder Method") In Class.

class Garage:
    def __init__(self):
        self.car = []

    def __len__(self):
        return len(self.car)

    def __getitem__(self, item):
        return self.car[item]

    def __repr__(self):
        return f"Garage : {self.car}"

    def __str__(self):
        return f"This Garage Has {len(self.car)} Vehicles"


Garage_1 = Garage()
Garage_2 = Garage()
Garage_1.car.append("Ford")
Garage_1.car.append("Audi")
Garage_1.car.append("Swift")
print(Garage_1.car)
print(len(Garage_1.car))
print(Garage_1.__class__)

Garage_2.car.append("Apache")
Garage_2.car.append("Bullet")
print(Garage_2.car)
print(len(Garage_1.car))  # We can use this also for getting length.
print(len(Garage_2.car))

# We used __len__ method to know Garage_1 object length
print(len(Garage_1))


# Using [] bracket notation

print(Garage_1.car[0])

# or we can add __getitem__ method in class.

print(Garage_1[2])


# __repr__ and __str__ methods In Class

""" `__repr__` should be used to print out a string representing the object such that 
with that string you can re-create the object fully."""

print(repr(Garage_1))
print(repr(Garage_2))

"""`__str__` should be used when printing the object out to a user,
 for example—can be more descriptive or even miss out some details."""

print(str(Garage_1))
print(str(Garage_2))


# Difference between str and repr

"""str() is used for creating output for end user 
while repr() is mainly used for debugging and development. 
repr’s goal is to be unambiguous and str’s is to be readable. 
For example, if we suspect a float has a small rounding error,
repr will show us while str may not."""