# . Write a Python program with a Student class that has an __init__ method for initializing attributes and a destructor method (__del__).
class Student:
    def __init__(self ,name ,age):
        self.name = name
        self.age  = age
        print(f"it is {self.name}inintializing atributes")
    def show(self):
        return f"display student details {self.name} and ,age : {self.age}"
    def __del__(self):
        print(f"teh student  {self.name} and {self.age} distroyed")
        
obj = Student('vaibhav', 22)
print(obj.show())

del obj