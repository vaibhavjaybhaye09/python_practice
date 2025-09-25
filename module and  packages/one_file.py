
def add(x,y):
    return  x + y
    
def sub(x,y):
    return x - y

def mulp(x,y):
    return x * y

def div(x,y):
    return x / y

def palindrome(x):
    original = x
    reversed_num = 0
    # Reverse the number
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    # Check if original and reversed are equal
    return original == reversed_num

# Example usage
x  = int(input("Enter a number: "))
if palindrome(x):
    print(f"{x} is a palindrome")
else:
    print(f"{x} is not a palindrome")
    
