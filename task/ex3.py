# Create a class Employee with a class variable company_name and 
# instance variables like name, salary. Demonstrate class variables vs instance variables.
class Employee:
    company = 'tech'
    def __init__(self , name ,salary):
        self.name = name
        self.salary = salary
    
    def show(self):
        
          return f"the company is : {Employee.company} and Employee name is {self.name} and the salary is {self.salary}"
    

emp1 = Employee('vaibhav',25000)
emp2 = Employee('akash',333000)

print(emp1.show())
print(emp2.show())
         
