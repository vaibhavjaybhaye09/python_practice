# Example?
# parameterize constucter  =to pass parameter 
class cal:
    def __init__(self,a,b):
        
        self .a = a
        self .b = b
        print(f"the addition is :{a+b}")
        

math = cal(9,5)
        

#default constucter
class map :
    def __init__(self):
        self.a = 4
        self.b = 5
        
        print(f"addtion of the number :{self.a+self.b}")
    
    
let = map()
        

# constucter with default arguments
class both :
    def __init__(self ,a =5 ,b=6):
        self.a = a
        self.b = b
        print(f"addtion is : {a+b}")

obj = both()

#deconstucter = destroy constucter delete constucter
class student :
    def __init__(self ,name , age):
        self.name = name
        self.age = age
        
        print(f"student name :{name}  And student age is :{age}")
    
s1 = student("vaibhav", 90)
# >>>>>>>   
del s1


class class1 :
      def __init__(self, name ,mark):
         self.name = name
         self.mark = mark
         print(f"the name is : {name} the aga is : {mark}")


ghi = class1("vibahv", 22)

del class1
# using construictor calculater create
class  clacu :                  # it is class
    def __init__(self , a ,b):  # init method
        self.a = a
        self.b = b
    def add(self):
        return f"addition :{self.a + self.b}"
    def sub(self):
        return f"substraction :{self.a - self.b}"
    def mulp(self):
        return f"multipliction :{self.a * self.b}"
    def div(self):
        return f"division :{self.a / self.b}"
   
obj2 = clacu(3,5)               #construictor call  
                  #with help of object method call
print(obj2.add())               
print(obj2.sub())
print(obj2.mulp())
print(obj2.div())
