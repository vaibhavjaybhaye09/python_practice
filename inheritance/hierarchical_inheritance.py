
# To demonstrate hierarchical inheritance, you should create instances of the child classes (son and daughter), not the parent.
# Also, the parent class should initialize hname in the constructor (__init__).

class parent:
    def __init__(self, hname):
        self.hname = hname

class son(parent):
    def son(self):
        return f"{self.hname} is my home"

class daughter(parent):
    def daughter1(self):
        return f"{self.hname} is my home"

# Create instances of the child classes
show_son = son('vaibhav')
print(show_son.son())

show_daughter = daughter('vaibhav')
print(show_daughter.daughter1())