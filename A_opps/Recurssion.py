# Recursion = a function that solving a problem by 
# calling itself on a smaller version of the same way.
def facto(n):
    if n == 0:
        return 
    
    print(n)
    facto(n-1)

print(facto(5))
