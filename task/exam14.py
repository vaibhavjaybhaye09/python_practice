# Create a custom exception class InvalidAgeError.
# Write a function that raises this exception if the age is less than 18 and handle it.
class ValidError(Exception):
    def __init__(self, age):
        super().__init__( f"Invalid age: {age} . Age must be 18 older")
        self.age = age
        

def check (age):
    if age < 18:
        raise ValidError(age)
    else:
        print("Access granted. age is valid")

try:
    user_age = int(input("entrt the age : "))
    check(user_age)
    
except ValueError as e :
    print("Error", e)
        
        