
# abstraction = avoiding security issues by,hiding unnecessary details and exposing only essential features of user interface.
# abstract class = is the class that contains one or more abstract methods.
#abstract method = it is a method that is declared but contains no implementation. An abstract method is defined using the `@abstractmethod` decorator from the `abc` module in Python.
#syntax
# from abc import ABC, abstractmethod
# class Base(ABC):   # create abstract class
#     @abstractmethod   # create abstract method
#     def show(self):
#         #body of abstract method
#         pass  # abstract


from abc import ABC, abstractmethod
class Shape(ABC):     # abstract class
    @abstractmethod   # abstract method
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
        def area(self):
            return self.length * self.width
        
        def perimeter(self):
            return 2 * (self.length + self.width)
        
#instantiate the class is object 
rect  = Rectangle(5, 10)
print("Area of rectangle is : ", rect.area())
print("Perimeter of rectangle is : ", rect.perimeter())

#what is abstraction
#whta is abstract class, what  is abstract method#
# write a program ro given string is palindrome or not with the help of abstraction