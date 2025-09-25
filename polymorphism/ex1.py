#super method = "The super() function in Python is used to call a method from a parent class."


class parent1:
    def show(self, a , b):
        return f"this is value of {a} and {b}"
        
class chil1(parent1):
    def show(self, a , b):
        super().show(a,b)
        return f"this is value of { a + b} in child "

obj4 = chil1()
print(obj4.show(10,20))

