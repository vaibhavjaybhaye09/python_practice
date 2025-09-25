# Demonstrate composition by creating a Car class with an object of the Engine class as an 
class Engine:
    def __init__(self, type):
        self.type = type
    
    def run(self):
        return f"{self.type} engine is running"

class Car:
    def __init__(self, brand, engine_type):
        self.brand = brand
        self.engine = Engine(engine_type)  # Composition: Engine object as attribute
    
    def drive(self):
        return f"{self.brand} car: {self.engine.run()}"

# Example usage
my_car = Car("Honda", "Petrol")
print(my_car.drive())