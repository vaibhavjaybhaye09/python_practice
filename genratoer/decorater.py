# def decrator_function(original_funcion):
#     def wrapper_function():
#         print("i like you")
#         original_funcion()
#         print("i like python programming")
        
    
#     return wrapper_function

# @decrator_function
# def original_function():
#     print("my name is vaibhav")
    

# original_function()


def answer(answer_function):
    def queton():
        print("the anser is = 200")
        answer_function()
        print("the 200 answr is the  answer function")
        
        
    
    return queton

@answer
def answer_function():
    print("the quetion is 100 + 100")
    

answer_function()


# what it is iterator    
#what is decorator     and both diffrence betweeen
# what is 