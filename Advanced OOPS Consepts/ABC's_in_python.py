# ABC:- Abstract Base Class

from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    def walk(self):
        print('Walking....')
    
    @abstractmethod
    def legs_num(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def legs_num(self):
        return 4
    

class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    def legs_num(self):
        return 2



#a = Animal()
 # Error: Can't instantiate abstract class Animal with abstract methods legs_num
#print(a.legs_num())  # We Can't Do This

d = Dog('Dog1')
print(d.legs_num())
d.walk()
m = Monkey("Monkey1")
print(m.legs_num())
m.walk()


# We Can Do This Amazing Thing With This.

animals = [Dog('Rony'), Monkey('Tomy')]

for a in animals:
    print(a.legs_num())