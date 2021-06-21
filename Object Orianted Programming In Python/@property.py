# @property

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    @property
    def average(self):
        return sum(self.marks) / len(self.marks)

vishal = Student("Vishal Parmar","Axar")
print(vishal.name)
vishal.marks.append(90)
vishal.marks.append(80)
vishal.marks.append(55)

# using @property we can make a method into value or property.
# Instead of vishal.average() we can write vishal.average.
print(vishal.average)

"""
You can do that with any method that doesn’t take any arguments. 
But remember, this method only returns a value calculated from the object’s properties.
If you have a method that does things
(e.g. save to a database or interact with other things), 
it can be better to stay with the brackets.

Normally:

* Brackets: this method does things, performs actions.
* No brackets: this is a value
(or a value calculated from existing values, in the case of `@property`).
"""