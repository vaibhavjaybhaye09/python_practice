# to Book ticket in Book my show 35

#condition:---> first it should ask theaters name then it should display the movie available then

#it has to display ticket price and in the end ticket should be booked


print("Welcome to Book My Show")
print("Please select a theater:")
print("1. kavreve Cinemas")
print("3. deccan Cinemas")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    print("You selected kavreve Cinemas")
    print("Available movies:")
    print("1. Movie A")
    print("2. Movie B")
    print("3. Movie C")
    
    movie = input("Enter the movie number (1-3): ")
    if movie == "1":
        price = 150
        print("You selected Movie A price =",price)
        
    elif movie == "2":
        price = 200
        print("YOu selected Movie B  price =",price)
    else:
        price = 250
        print("You selected Movie C price =",price)
        
        
elif choice == "2":
    print("deccan Cinemas")
    print("Available movies:")
    print("1. Movie D")
    print("2. Movie B")
    print("3. Movie C")
    
    movie = input("Enter the movie number (1-3): ")
    if movie == "1":
        price = 150
        print("You selected Movie A price =", price)
    elif movie == "2":
        price = 200
        print("YOu selected Movie B price =", price)
    else:
        price = 250
        print("You selected Movie C price =", price)
        
else: 
    print("Invalid choice. Please select a valid theater not avaible.")
    