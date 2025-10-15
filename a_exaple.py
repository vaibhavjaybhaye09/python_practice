# reverse string
s = 'vaibhav'
print(s[::-1])
# reverse list
s1 = [1,2,3,4,5]
print(s1[::-1])
# palindrome
def palindrom(pk):
    if pk == pk[::-1]:
         return f"is_palindrome {pk}"
    else:
         return f"not_palindrome {pk}"  
print(palindrom('vaibhav'))
print(palindrom('madam'))

# count vowels
def count(pk):
    vow = 'AEIOUaeiou'
    count = 0
    for n in pk :
        if n in vow:
            count = count + 1 
            print(count)
    return count
print(count('vaibhav'))

# frequency of characters in string
def frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char,0)+1
    return freq
print(frequency('vaibhav'))

# anagram
def anagram(str1, str2):
    return sorted(str1) == sorted(str2) 
print(anagram('vaibhav', 'vaibhav'))

# s = 'vaib,hav'
# # print(s.capitalize())

# s1 =  ['11','2','34','5']
# # for i in s1:
#     # print(i.isdigit())
# print(min(s1))
# print(max(s1))
# print(sum(map(int,s1)))
# def no(pk):
#  return list(set(pk))
 
# print(no( ['11', '2', '34', '5', '2', '11']))


# inheritance = it is a process of acquiring the properties and behaviors of parent class to child class
# it is achived by creating a parent class and child class
class Car :
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand

d = Car('swift','suzuki')
print(d.brand)

# single inheritance = it is  single parent and single child class
class Car:
  def show(self):
    print("Car")
class Bike(Car):
    pass
b =Bike()
b.show()

# multilevel inheritance = it is  single parent and single child class
class Grandfather:
    def show(self):
        print("Grandfather")
class Father(Grandfather):
   pass
class Son(Father):
    pass
c = Son()
c.show()

# multiple inheritance = it is  multiple parent and single child class
class  Father1:
    def show(self):
        print("Father1")
class Mother1:
    def display(self):
        print("Mother1")
class child(Father1,Mother1):
    pass
d = child()
print(d.show())
print(d.display())

# abstraction = it is hinding the internal details and showing only  the functionality to the user
# it is achived by abstract class and abc modeule in Python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
          def __init__(self, width, height):
            self.width = width
            self.height = height
          def area(self):
            return self.width * self.height
r  = Rectangle(5, 10)
print(r.area())

# encapsulation = it is binding the data and methods into single unit
# it is achived by private and protected access modifiers
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())



#find missing number
def find(arr, n):
    total = n * (n + 1) // 2
    return total - sum(arr)

print(find([1, 2, 4, 5], 6)) # Output: 3