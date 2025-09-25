#  Create a BankAccount class with a private balance attribute 
# and provide public getter and setter methods to interact with it (encapsulation).

class BankAccount :
      def __init__(self,balance , holder):
            self.holder = holder
            self.__balance = balance
      def getter(self):
          return self.__balance
      
      def show(self):
          print(f"name = {self.holder} and balance is {self.__balance}")
          
      def Deposite(self,amount):
          if amount > 0 :
            self.__balance = self.__balance + amount
            print(f"Dposite amount is = {amount}  New balance is = {self.__balance}")
          else:
              print("invalid amount!!!")
              
              
      def Widthdraw(self,amount):
          if amount > 0 :
              self.__balance = self.__balance - amount
              print(f"the widthdraw amount is = {amount} the updated balnce is = {self.__balance}")
          else :
              print("invalid amount")
              
              
obj =  BankAccount(2000,'vaibhav')
obj.show()
obj.Deposite(500)
obj.Widthdraw(2000)