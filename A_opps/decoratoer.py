# Decoretor = Its in pyhton is a way to add extra behaviour to a function without changing a function  codes




def decorato(x):
    def acc(v):  #wrapper accepts argument 
        sum = 2 + 2  #extra behaviour
        ok = x(sum) #call original funtion
        return ok
    return acc

@decorato
def done(value):
    return value + 4

print(done(0))


def vai(x): #decorator takes function
    def sol():
        sum = 2 + 2
        return sum
        x() #call originall funtion
    
    return sol


@vai
def ok(sum):
    return sum + 4


ok() #vcall decorated function




# *args → extra positional arguments (tuple)

# **kwargs → extra keyword arguments (dictionary)



def snii(*args): # takes 
    total = 0
    for i in args:
        total += i
    return total

print(snii(1,2,3,4,5))