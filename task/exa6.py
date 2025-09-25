#  Demonstrate Method Resolution Order (MRO) with multiple inheritance. Create classes ClassA, ClassB, and ClassC 
# and display the method calling order.

class A:
    def show(self):
        print("A")
class B(A) :
    def show(self):
        print("B")
        super().show()
class c(A):
      def show(self):
          print("C")
          super().show()
        
class D(B,c):
    def show(self):
        print("D")
        super().show()

obj = D()
obj.show()
