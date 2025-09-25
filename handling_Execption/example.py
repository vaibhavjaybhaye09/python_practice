try:      # try = it is the bllock of code that may raise an exception
    x = int(input("Enter a number:"))
    y = int(input("Enter a number:"))
    z = x / y
    print(z)

except ZeroDivisionError:  # except = it is the block of code that will execute if an exception occurs
    print("Not divisible by zero")

else:   # else = it is the block of code that will execute if no exceptions occur
    print("program executed successfully")
finally:  # finally = it is the block of code that will always execute
    print("This will always execute")
    print("End of program")