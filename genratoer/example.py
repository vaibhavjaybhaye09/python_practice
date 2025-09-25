# def num():
#     for i in range(0,100,2):
#         print(i)
        
# num()




# def creator():
#     number = 0
#     while number <= 100:
#         yield number
#         number = number + 5

# print(creator())
# x = creator()
# print(next(x))
# print(next(x))
# print(next(x))


def fibo():
    a = 0
    b = 1
    for i in range (10):
        print(a,end = " ") 
        a,b = b, a+ b
        
fibo()
    