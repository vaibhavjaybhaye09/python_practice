# hybrid inheritance  = we have one child class and multiple parent classes and one parent class is child of another parent class
class parent1:
    def home(self,hname):
        self.hname = hname
class son(parent1):
    def myhome(self):
        return f"the home is : {self.hname}"
class daughter(parent1):
    def myhome1(self):
        return f"the home is : {self.hname}"

class child(son,daughter):
    def home2(self):
        return f" the home is : {self.hname}"
    

family = son()
family.home("vaibhav home")
print(family.myhome())

family1 = daughter()
family1.home("vaibhav home")
print(family1.myhome1())

family = child()
family.home("vaibhav home")
print(family.home2())