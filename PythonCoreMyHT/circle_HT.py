# Your task is to create a Circle constructor that creates a circle with a radius provided by an argument.
# The circles constructed must have two getters getArea() (PIr^2) and 
# getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).
# For help with this class, I have provided you with a Rectangle constructor which you can use as a base example.
# Notes Round results up to the nearest integer.
# Examples
# circy = Circle(11)
# circy.getArea()
# Should return 380.132711084365
# circy = Circle(4.44)
# circy.getPerimeter()
# Should return 27.897342763877365

from math import pi


class Rectangle:

    def __init__(self, sideA=0, sideB=0):
        self.sideA = sideA
        self.sideB = sideB

    def getArea(self):
        return self.sideA * self.sideB

    def getPerimeter(self):
        return 2 * (self.sideA + self.sideB)


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return round(pi*self.radius**2)

    def getPerimeter(self):
        return round(2*pi*self.radius)
        
circy = Circle(4.44)
circy.getArea()
print(circy.getArea())
print(circy.getPerimeter())