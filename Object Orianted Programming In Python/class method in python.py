"""
class method:

A class method is a method which is bound to the class and not the object of the class.
They have the access to the state of the class as it takes a class parameter that
points to the class and not the object instance.
It can modify a class state that would apply across all the instances of the class.
For example it can modify a class variable that will be applicable to all the instances.

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Hello {self.name}"

    @classmethod
    def Details_Class(cls, name, age):
        return cls(name, age)


    @staticmethod
    def Details_static(name, age):
        return name, age

o1 = Person.Details_Class("Vishal", 19)

print(o1)

o2 = Person("Sanjay", 17)
print(o2)

print(Person.Details_static("Harsh", 20))


"""
staticmethod:

A static method is also a method which is bound to the class and not the object of the class.
A static method can’t access or modify class state.
It is present in a class because it makes sense for the method to be present in class.

"""