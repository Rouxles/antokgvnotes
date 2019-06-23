import math

class Circle:
    def __init__(self, radius):
        self.radius = int(radius)

    def getArea(self):
        return self.radius*self.radius*math.pi

    def getCircumference(self):
        return (self.radius)*2*(math.pi)


value = int(input("hi"))
my_circle = Circle(value)
print(my_circle.radius)
print(my_circle.getArea())
print(my_circle.getCircumference())
