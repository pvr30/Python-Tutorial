class Shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def show_parameters(self):
        return f"Length = {self.length}\nBreadth = {self.breadth}"


class Rectangle(Shape):
    def __repr__(self):
        return f"Area Of Rectangle : {self.length * self.breadth}\nPerimeter Of Rectangle : {2 +(self.length + self.breadth)}"

class Cuboid(Shape):
    def __init__(self, length, breadth, height):
           Shape.__init__(self, length, breadth)
           self.height = height

    def __repr__(self):
        return f"Volume Of Cuboid : {self.length * self.breadth * self.height}"

class Square():
    def __init__(self, length):
        self.length = length

    def area_of_square(self):
        return f"Area Of Square : {self.length * self.length}"

rectangle = Rectangle(8, 10)
print(rectangle)


cuboid = Cuboid(10, 20, 30)
print(cuboid)

square = Square(10)
print(square.area_of_square())

