# Classes And Objects In Python

"""class Person:
    pass

vishal = Person() # Here vishal is an object of Person Class.

vishal.name = "Vishal Parmar"
vishal.age = 19

print(vishal.name)
print(vishal.age) """

# self
"""Class methods must have an extra first parameter in method definition.
We do not give a value for this parameter when we call the method, Python provides it.
If we have a method which takes no arguments, then we still have to have one argument.
When we call a method of this object as myobject.method(arg1, arg2), 
this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) 
– this is all the special self is about."""


class Person:
    def print_details(self):
        print(f"First Name: {self.first_name}\nLast Name : {self.last_name}")
        print(f"Age :{self.age}")

vishal = Person()
vishal.first_name = "Vishal"
vishal.last_name = "Parmar"
vishal.age = 19

vishal.print_details()
print("\n")
Person.print_details(vishal)

print("\n Explanations Of Constructor")
# __init__ method or Constructor .

class Person:
    def __init__(self,first_name,last_name,age):
        self.first = first_name
        self.last = last_name
        self.age = age

    def print_person_details(self):
        return f"Name:{self.first} {self.last}\nAge: {self.age}"

harsh = Person("Harsh","Parmar",20)
vishal = Person("Vishal","Parmar",19)

# we can call function of class by object name.
print(harsh.print_person_details())

# or we can call function of class by passing an object in Class Name.
print(Person.print_person_details(vishal))


