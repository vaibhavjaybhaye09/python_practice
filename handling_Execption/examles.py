# try:
#   y = int(input("enter a number: " ))
#   x = int(input("enter a number: "))
#   z = y / x
#   print(z)
# except ZeroDivisionError:
#        print("Error: Division by zero is not allowed.")
# except ValueError:
#         print("Error: Invalid input. Please enter a valid number.")
# else:
#     print("the code has successfully run")
    

# try: 
#     name = "vaibhav"
#     my_list = [1,2,3,4,5]
#     print(name)
#     print(my_list[5])

# except NameError:
#     print("Name is not defined")
# except IndexError:
#     print("Index is out of range")
# else:
#     print("code run successfully")
    

class InvalidAgeError(Exception):
    """Exception raised for invalid age input."""

    def init(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().init(self.message)  
try:
    age = int (input("enter a age"))
    if not (0 <= age <=21):
        raise InvalidAgeError(age)
    else:
        print("valid age")
except InvalidAgeError as e:
    print(f"InvalidAgeError : {e.message} (age : {e.age})")
else:
    print("eligible")
finally:
    print("rest of the code")
    