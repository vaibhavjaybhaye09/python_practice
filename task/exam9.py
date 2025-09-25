# Define a ComplexNumber class with attributes real and imaginary. 
# Overload the + operator to add two complex numbers and the str() method for string representation.
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        return f"{self.real} - {abs(self.imaginary)}i"

# Example usage
if __name__ == "__main__":
    c1 = ComplexNumber(3, 4)
    c2 = ComplexNumber(1, -2)
    result = c1 + c2
    print(f"Complex number 1: {c1}")
    print(f"Complex number 2: {c2}")
    print(f"Sum: {result}")