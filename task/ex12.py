#  Write a class Person with a class method from_string(cls, string) to create an instance from a formatted string.
#  Also, write a method decorator that logs the method name and arguments.
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    @classmethod
    def from_string(cls,string):
        name, age, city, = string.spilit(",")
        return cls(name.strip(), age.strip(), city.strip())
    
    def show(self):
        print( f"my name is {self.name} and my age is {self.age} and my city is {self.city}")
        
    
obj = Person("vaibhav", 33 ,"Pune")
obj.show()
        
                