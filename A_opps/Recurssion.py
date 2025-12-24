# Recursion = a function that solving a problem by 
# calling itself on a smaller version of the same way.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1) 

print(factorial(5))  # Output: 120