"""class Garage:
    def __init__(self):
        self.car = []


    def __len__(self):
        return len(self.car)


    def add_car(self, car):
        raise NotImplemented("Here No Car In Garage At This Time")"""

#print(Garage().add_car("Swift"))

# Output :  TypeError: 'NotImplementedType' object is not callable.

"""
That way we can’t call the method and assume it works—it will 
now fail and crash our program. We’ll know that 
we’re doing something that won’t work
(because it’s not implemented yet).
That’s how you `raise` an error: use the keyword and create a
new error object from the class you want. All built-in errors
are available everywhere for you to use.

"""

class Car:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Car : {self.name}"

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects.')
        self.cars.append(car)


swift_garage = Garage()
swift = Car("SWIFT")
print(swift)
swift_garage.add_car(swift)
swift_garage.add_car("BMW") # error
print(len(swift_garage))