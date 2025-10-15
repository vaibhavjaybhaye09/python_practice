def find(arr, n):
    total = n * (n + 1) // 2
    return total - sum(arr)

print(find([1, 2, 3, 4, 6], 6)) # Output: 5

#overloading
class Ovr:
    def add(self,*num):
        return sum(num)
c = Ovr()
print(c.add(12,2,2,3,44))


#verrinding
class Bird:
    def sound(self):
        return "chipp"
class Dog(Bird):
    def sound(self):
        return "bark"

d = Dog()
print(d.sound())


# inhertance   
class Father:
    def show(self):
        print("Father")

class Son(Father):
    pass
s = Son()
print(s.show())

# multiple inheritance
class A:
    def show(self):
        print("a")
class B :
    def show1(self):
        print("b")

class chils(A,B):
    pass

c = chils()
print(c.show())
print(c.show1())


# multilevel inheritance
class Grandfather:
    def show(self):
        return "GrandFather"
    
class Father(Grandfather):
         pass
class Child(Father):
      pass
c = Child()
print(c.show())


n = 23
if n % 2 == 0:
    print("even")
else:
    print("odd")



