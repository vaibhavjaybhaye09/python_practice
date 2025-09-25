
#    top to bottom approach


# object oriented programming language python
#    because it is support object and class


#    bottom-up approach

# class and object
## class is a collection of attributes and methods
# class is a blueprint for creating objects
# object is real time implementaion  of a class


# inheritance  @ polymorphism @ encapsulation @ abstraction 

class number :   # create class name
    c = 7
    y = 90
    
obj = number()  # create object of class  u can any name of object
print(obj.c , obj.y)  # access class variable using object


class Student:  # crveate class name
    name = "Vaibhav Jaybhaye"  # class variable:
    marks = 90  # class variable
    age = 21  # class variable

# object method
stu = Student()  
print(stu.age + stu.marks)



# methods in class
## method is a function defined inside a class
#dynamic method
# is a merhocd that can be called on an object of the class
class value:
    def add(self,a,b):
        return a+b
    
obj1 = value() # create object of class   
obj1.add(5, 10)#  # call method using object



class value1:
    def division(self, a, b):
        
        return a/b
oobj2 = value1()
oobj2.division(10, 5)  # call method using object

#dynamic method
class number1:
    def addition(self, a, b):
        return a + b
    @classmethod  # class method
    def subtraction(cls, a, b):
        print("This is class method")
        
    @staticmethod #static method
    def name():
        print("hello vaibhav")
        
std1 = number1
print(std1.name())

obj3 = number1()  # create object of class
print(obj3.addition(10, 5))  
print(obj3.subtraction(10, 5))  

#class method
# class method is a method that is bound to the class and not the object
class add:
    @classmethod
    def plus(cls, a, b):
        return a + b
    
obj4 = add()  
print(obj4.plus(10, 5))  # call class method using object


class demo :
    def d1(self):
        return"thid is dynamic method"
    @classmethod
    def d2(cls):
        return "this is class mthod"
    @staticmethod
    def d3():
        return "this is static method"
    

ojd = demo()
ojd.d1()
ojd.d3()
ojd.d2()
     
class claculater:
    def addition3(self , a ,b):
        return f"addition of two number: {a+b}"
    def sub(self ,a,b):
        return f"is dub two number:={a-b}"
    def mulp(self,a,b):
        return f"it is multiplication of twonumber {a * b}"
    def div(self,a,b):
        return f" it is two number oof division{a/b}"

math = claculater()
math.addition3(5,6)
math.sub(10,5)
math.mulp(2,2)
math.div(5,90)



#  whta is obeject and class explain with example
#  whtat is the diifrence between oops aNd pop
#  what id diiffrnt types of function
#  whhat is difference between user defined function and built in function
#                                 user defined function and lambda function
                                #   print and return a
                                
                                
            
