# 5. Demonstrate multiple inheritance with a Person class and an Employee class
# , where Employee inherits from Person.

class Person :
    def __init__(self,name ,age):
        self.name = name
        self.age = age
    
    def show(self):
        return f"the name {self.name}  , Age : {self.age}"
    
class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
    
    def display(self):
         return f"the employee department is : {self.dept_name}"
     
     
class Employee(Person , Department) :
    def __init__(self, name, age,dept_name,empid ):
        
        Person.__init__(self,name,age)
        Department.__init__(self , dept_name)
        
        self.empid = empid
        
    def info(self):
        return f"{self.show()} ,  {self.display}  , Employee id = {self.empid} "
    

obj = Employee('vaibhav',22 ,'IT', 180999)
print(obj.info())