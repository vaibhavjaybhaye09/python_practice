#  Create a Vehicle class with a method info(). Derive a Car class, 
#  override the info() method, and use super() to call the base class method.
class Vehicle:
    def info(self):
        print("this is vehicle")
        
class car(Vehicle):
    def info(self):
        super().info()
        print("this id car")
        

    
    
v = car
v.info()