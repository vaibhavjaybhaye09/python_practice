#  Create an abstract class Shape with an abstract method area().
#  Derive Circle and Rectangle classes and implement the area() method.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def circle(self):
        pass
    
    @abstractmethod
    def rectangle(self):
        pass

class Count(Shape):  # Class name should be capitalized as per convention
    def __init__(self, length, radius, width):  # Corrected spelling of 'radius'
        self.length = length
        self.width = width
        self.radius = radius  # Corrected spelling
        
    def circle(self):  # Proper method indentation
        return self.radius * self.radius * 3.14
        
    def rectangle(self):  # Proper method indentation
        return self.length * self.width

area = Count(3, 4, 5)  # Corrected class name
print("Area of circle is", area.circle())
print("Area of rectangle is", area.rectangle())