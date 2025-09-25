# Car Rental System

available_cars = {
    101: ('Toyota', 30.00),
    102: ('Honda Civic', 28.00),
    103: ('Ford Focus', 32.00),
    104: ('Chevrolet Malibu', 25.00),
    105: ('Nissan Altima', 29.00),
    106: ('Hyundai Elantra', 27.00),
}

rented_cars = []
rental_records = []

def view_available_cars():
    print("\nAvailable Cars:")
    if not available_cars:
        print("No cars available for rent. Please check back later.")
    else:
        for car_id, (model, price) in available_cars.items():
            print(f"Car ID: {car_id}, Model: {model}, Price per Day: ${price:.2f}")

def rent_a_car():
    if not available_cars:
        print("No cars available for rent.")
        return

    try:
        car_id = int(input("Enter the Car ID you want to rent: "))
        if car_id not in available_cars:
            print("Invalid Car ID. Please try again.")
            return

        username = input("Enter your name: ").strip().lower()
        days = int(input("Enter the number of days you want to rent: "))

        if days <= 0:
            print("Invalid number of days. Please enter a positive number.")
            return

        model, price = available_cars.pop(car_id)
        total_cost = days * price

        rented_cars.append((username, car_id, model, days, total_cost))
        rental_records.append((username, car_id, model, days, total_cost))

        print(f"\nYou have successfully rented {model} for {days} days.")
        print(f"Total cost: ${total_cost:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def view_rented_cars():
    print("\n------ Rented Cars ------")
    if not rented_cars:
        print("No cars are currently rented.")
    else:
        for record in rented_cars:
            username, car_id, model, days, total_cost = record
            print(f"Car ID: {car_id}, Model: {model}, Rented by: {username}, Days: {days}, Cost: ${total_cost:.2f}")

def return_a_car():
    username = input("Enter your name to return a car: ").strip().lower()
    found = False
    for i, record in enumerate(rented_cars):
        if record[0] == username:
            found = True
            car_id = record[1]
            model = record[2]
            days = record[3]
            total_cost = record[4]
            price_per_day = total_cost / days
            available_cars[car_id] = (model, price_per_day)
            rented_cars.pop(i)
            print(f"{model} has been returned successfully. Thank you, {username}!")
            break
    if not found:
        print(f"No rented car found for user '{username}'. Please check your name.")

def view_rental_history():
    username = input("Enter your name to view rental history: ").strip().lower()
    found = False
    print("\n------ Rental History ------")
    for record in rental_records:
        if record[0] == username:
            print(f"Car ID: {record[1]}, Model: {record[2]}, Days: {record[3]}, Total Cost: ${record[4]:.2f}")
            found = True
    if not found:
        print(f"No rental history found for user '{username}'.")

def exit_app():
    print("Thank you for using the Car Rental System. Goodbye!")
    exit()

def operation(choice):
    if choice == 1:
        view_available_cars()
    elif choice == 2:
        rent_a_car()
    elif choice == 3:
        view_rented_cars()
    elif choice == 4:
        return_a_car()
    elif choice == 5:
        view_rental_history()
    elif choice == 6:
        exit_app()
    else:
        print("Invalid choice. Please select a number from 1 to 6.")


# Main Loop
while True:
    print("\n------ Car Rental Menu ------")
    print("1. View Available Cars")
    print("2. Rent a Car")
    print("3. View Rented Cars")
    print("4. Return a Car")
    print("5. View Rental History")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice (1-6): "))
        operation(choice)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
