sen = "My name is John Doe and I live in New York City."
print(len(sen)) # count the number of characters in the string and spacees

print(sen.lower()) # convert the string to lowercase

print(sen.upper()) # convert the string to uppercase

print(sen.capitalize()) # capitalize the first letter of the string

print(sen.index("City")) # find the index of the substring 'City'

print(sen.replace("John", "Vaibhav")) # replace 'John' with 'Vaibhav'

print(sen.split()) # split the string into a list of words

print(sen.find('Vaibhav')) # find the index of the substring 'Vaibhav', returns -1 if not found

print(sen.casefold()) # convert the string to lowercase, similar to lower() but more aggressive
 
print(sen.rindex("vaibhav")) # find the last index of the substring 'vaibhav', raises ValueError if not foundpr
print(sen.rfind("vaibhav")) # find the last index of the substring 'vaibhav', returns -1 if not found
print(sen.strip()) # remove leading and trailing 

#slicing 
n = "1,2,3,4,5,6,7,8,9,0"
print(n[0:5])
print(n[5:]) # slicing from index 5 to the end
print(n[:5]) # slicing from the start to index 5
print(n[-1]) # get the last character
print(n[-2:]) # get the last two characters
print(n[::2]) # get every second character
print(n[::-1]) # reverse the string
print(n[1:8:2]) # get characters from index 1 to 8 with a step of 2
print(n[1:8:-2]) # this will not return anything as the step is negative and start is less than end
print(n[::]) # get the whole string
print(n[::3]) # get every third character
print(n[1:8:3]) # get characters from index 1 to 8 with a step of 3
print(n[1:8:-3]) # this will not return anything as the step is negative and start is less than end
print(n[1:8:2]) # get characters from index 1 to 8 with a step of 2  