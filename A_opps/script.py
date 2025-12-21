# name = "vaibhav"
# age = 28

# print(type(name))
# print(type(age))


# its method is to group related data and functions together

class Dog: # calss defination = its like a blue print of object 
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print("bhoo bhoo")



dog1 = Dog("Buddy", "Golden Retriever") # object creation its reealtime implementation of class
dog1.bark()

print(dog1.name)
print(dog1.breed)
