# number =[1,2,3,4,6,7]
# print( [x ** 2 for x in number])

# # multiply the each number
# num = [1,2,3,4,5]
# print([x * 2 for x in num])

# # addition of number in list
# print([x + 2 for x in num])


# print([x for x in range(51) if x % 2 == 0])

# print([ x  for x in range(21)])

label = [f"\n even = {x} \n"  if x % 2 == 0 else f"\n odd = {x}" for x in range(51)]
print(label)