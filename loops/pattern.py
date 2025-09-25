 
# for i in range(6,0,-1):
#     print(i * "*")
    
# to write 1  to 50 no. even\
# sum = 0
# for i in range(1,51):
#     if i % 2 == 0:
#         sum = sum + i
# print("the numbers = ",sum)

# # write a program to first 20 number and their  square number
# for i in range(1,21): 
#     print(i,i*i)
    
# #write a program to  print the first 10 number odd
# i = 1
# while i <= 10:
#     if i % 2 !=0:
#         print(i)
#         i += 1
#     else:
#         i += 1

# # write a program to check a number is divisibel by  8 and 12 up to 100
# for i in range(1, 101):
#     if i % 8 == 0 :
#         print(i,"is divisible by 8")
#     elif i % 12 == 0:
#         print(i ,"is divisible by 12")
    
    
    
# # write a program to create to a biiling a system at super market
# name = input ("Enter the name of customer : ") 
# while True:
   
#     quantity = int(input("Enter the quantity if item :"))
#     price = int(input("Enter the price of each item: "))
#     total = 0
#     total += quantity * price
#     print(f"total price of {quantity} item is : {total}")
#     print(f"total price of {name } is : {total}")
#     repea =input("DO you want to continue yes or no :")
#     if repea.lower() == 'yes':
#         continue
#     else:
#         print("thanks for shopping please visit again")
#         break
    
    
# # write a program to check to hhow many time alpphabet o is occurring
# pra = input("Enter your name : ")
# count = 0
# for char in pra:
#     if char.lower() == 'o':
#         count = count + 1
# print(f"the  o is occurring {count} times in {pra}")

# string = input("Enter the string to change upper case : ").lower().strip()
# print(string.upper())
# print(string.lower())
# print(string.lower())
# print(string.title())


# write the program to find the index number of fit in 

# str = "fit in"
# print(str.index("t"))

for i in range(9,0,-1):
    for j in range(1, i + 1):
        print(i, end="")
    print()


for i in range(1,5):
    for j in range(1, i + 1):
        print(j, end =" ")
    print()