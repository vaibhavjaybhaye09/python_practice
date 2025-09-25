num  = int(input("Enter a number: "))
if num < 1:
    print("it is not prime number")
else:
    for i in range(2,11):
        if num % i == 0:
            print("it is not prime number   ")
            break
    else:
        print("it is prime number")
        
        
        
#fibbonacci series
a = 0
b = 1
print("Fibonacci series:")
print(a)
print(b)
for i in range(2, 11):
    c = a + b
    a = b
    b = c
    print(c)
    
    
# check palindrome or not 
num = int(input("Enter a number: "))
temp = num 
rev = 0
while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
    
if temp ==  rev:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")