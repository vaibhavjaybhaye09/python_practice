 # the inheritance is the process of acquiring the properties and methods of another class
#singal inheritance =  we have one child class and one parent class
 
# class demo :
#     def name(self):
#         print("this is demo class")
        
class cal :
    def number(self,a = 5 , b = 20):
        self.a = a
        self.b = b
        
class add(cal):
    def addition(self):
        return f"the addition of{self.a} and {self.b} is : {self.a + self.b}"
    

amth = add()
amth.number(10, 20)
amth.addition()




########################
# 
class std :
    def details(self,name ="vaibhav",age = 20):
        self.name = name
        self.age = age
class info(std):
    def show(self):
        return f"the name is :{self.name} and agee is :{self.age}"
    
student = info()
student.details("vaibhav", 20)
student.show()


#Multiple inheritance = we have one child class and multiple parent classes

class friend:
    def name1(self,name):
        self.name = name
        
class friend1 :
    def name2(self,name1):
        self.name1 = name1

class vaibhav(friend,friend1):
    def show2(self):
        return f"the name is my friend : {self.name} and 2nd is : {self.name1}"

v1 = vaibhav()
v1.name1("akash")
v1.name2("vaibhavi")


#multiplelevel inheritance = we have one parent class and multiple child class

class Gname:
    def name(self,name):
        self.name = name

class pname :
    def namep (self,namep):
        self.namep = namep
        
class child(Gname,pname):
    def show(self ,cname):
        self.cname = cname
        return f"the name is:{self.cname} and parent name is : {self.name} and parent name is : {self.namep}"
      
      
c1 = child("viabhav")
c1.namep("eknath")
c1.show("vikram")


#hir = we have one child class and one parent class and one grand parent class
class grandparent:
    def name(self,name):
        self.name = name
class parent(grandparent):
    def namep(self,namep):
        self.namep = namep

class child(parent):
    def show(self,cname):
        self.namec = cname
        return f"the name is granparent : {self.name} and parent name is : {self.namep} and child name is : {self.namec}"
    
g1 = child("vaibhav")
g1.namep("eknath")
g1.grandparent("vikram")