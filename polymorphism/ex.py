# polymorphism = "Polymorphism is the ability of different objects to respond to the same method call in different ways."

def add(*arg):
    return sum(arg)

print(add(1, 2 ))
print(add(1, 2, 3, 4))


#polymorphism in built-in function
print(len("vaibhav"))
print(len(["vinay", "vaibhav", "akash"]))




print(max(1, 2, 3, 4, 5, 6, 7, 8, 9, 5))
print(min("vaibhav", "vinay", "akash"))

# polymorphism in user-defined function
def show(num):
    return len(num)

print(show("vaibhav"))
print(show([1,2,3,4,5]))        
 
 
def dis(num,num1):
    print(num1 + num)
    return (num * num1)
    
print(dis(2,3))
print(dis(10,5.5))


# polymorphism in class & objects
class number:
    def add(self,num1,num2):
        return num1 + num2
     
obj1 = number()
print(obj1.add(2,5))
print(obj1.add(2.5,3.90))


#method overloading = "Method overloading is a feature that allows a
# class multiple method, but different parameters."
class calculator:
    def sum(self, a = 0 ,b = 0, c = 0):
        return a + b + c
    
obj2 =calculator()
print(obj2.sum(1))
print(obj2.sum(10,20))
print(obj2.sum(10,20,30))

class animal:
    def sound(self,sound):
        return f"the animal makes a {sound} sound"

ob = animal()
print(ob.sound("bark"))
print(ob.sound("bh"))
print(ob.sound("si;ng"))      
    
    
#overriding = "Overriding is 
# a feature that allows a subclass to provide a specific              
               # implementation of a method that is already defined in its superclass."


class parent:
    def show(self):
        return "this is parent class"
class child(parent):
    def show(self):
        return "this is child class"
    
obj3 = child()
print(obj3.show())


class parent1:
    def show(self, a , b):
        return f"this is value of {a} and {b}"
class chil1(parent1):
    def show(self, a , b):
        return f"this is value of { a + b} in child "

obj4 = chil1()
print(obj4.show(10,20))


#super method = "The super() function in Python is used to call a method from a parent class."


class parent1:
    def show(self, a , b):
        return f"this is value of {a} and {b}"
        
class chil1(parent1):
    def show(self, a , b):
        # Using super() to call the parent class method
        super().show(a, b)
        return f"this is value of { a + b} in child "

obj4 = chil1()
print(obj4.show(10,20))




# what is polymorphism in python?
# what is overloading in python?
# what is overriding in python?
# what is defrence between overloading and overriding?
# what is supermethod in python?