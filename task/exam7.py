# Write a class MathOperations that has both static methods and instance methods. 
# Show the difference by calling methods using the instance and class name.

class Math :
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    @staticmethod
    def addition(self):
        return self.x + self.y
    
    def sub(self):
        return self.x - self.y
    
    def mulp(self):
        return self.sub * self.y
    
    def div(self):
        return self.x / self.y
    

obj = Math(4 ,10)
print(obj.addition())
print(obj.sub())
print(obj.mulp())
print(obj.sub())