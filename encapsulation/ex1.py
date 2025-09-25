# encapsulation =  wrapping data and methods in a class to restrict access to them
class addition :
    def twonum(self, a , b):
        return a + b


obj = addition()
obj.twonum(10, 20)
# encapsulation = "Encapsulation is a fundamental concept in object-oriented programming that refers to the bundling of data and methods that operate on that data within a single unit, or class. It restricts direct access to some of an object's components, which can prevent the accidental modification of data."

#Access control = "Access control in encapsulation is the mechanism that restricts access to certain components of a class, allowing only specific methods to interact with the data. This is typically achieved using access modifiers like private, protected, and public."

# Access modifiers = "Access modifiers are keywords used in object-oriented programming to set the accessibility of classes, methods, and other members. Common access modifiers include public, private, and protected."
# Public Method = "Public members of a class can be accessed from anywhere in the program. They are not restricted and can be accessed directly."
class itpm :
    def __init__(self):
        self.course = "Da" 
        self.tech = "python"
    def show(self):
        return self.course +  self.tech 

obj1 = itpm()
print(obj1.show())

class itpm1 :
    def __init__(self):
        self.course = "BA"
        self.tech = "python"
    def show1(self):
        return self.course + self.tech
    
obj2 = itpm1()
print(obj2.show1())



class math :
    def __init__(self):
        self.x = 10
        self.y = 20
    def sum(self):
        return self.x + self.y
class math1 :
    def sub (self):
        return self.x - self.y
    
obj3  = math()



#protected Method = "Protected members of a class can be accessed within the class and by subclasses. They are not accessible from outside the class hierarchy."
#protected variable define with single underscore

class number :
    def __init__(self):
        self._x = 23
        self._y = 45
    def num1(self):
        return self._x
class number1(number) :
    def num2(self):
        return self._y

ob = number1()
print(ob.num1())
print(ob.num2())


class dog1:
    def __init__(self):
        self._name = "Dog"
        self._name2 = "Dog2"
    def dogn(self):
        return self._name
class dog2(dog1):
    def dogn2(self):
        return self._name2
    
obb  = dog2()
print(obb.dogn())
print(obb.dogn2())

# Private Method = "Private members of a class can only be it defined and accessed within the class itself. They are not accessible from outside the class or by subclasses. Private members are typically used to hide implementation details."
# Private variable define with double underscore

class abc :
    def nko(self):
        self.__name = "XYZ"
        return self.__name
obk = abc()
obk.nko()


# what is encapsulation  with example
#whta  are the access specifiers in python
# whta is difference between public, protected and private 
# write a program to print area ,perimeter of the Rectangle 1st make all veriable is public ,then protected and then private

