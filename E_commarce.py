# E-Commerce System using Python OOP

class Product:
    def __init__(self, pid, name, price, stock):
        self.pid = pid
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        print(f"Product ID: {self.pid}, Name: {self.name}, Price: ₹{self.price}, Stock: {self.stock}")

    def stocks(self, quantity):
        return self.stock >= quantity

    def reduce_stock(self, quantity):
        if self.stocks(quantity):
            self.stock -= quantity


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def display(self):
        return self.product.price * self.quantity


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        if product.stocks(quantity):
            self.items.append(CartItem(product, quantity))
            product.reduce_stock(quantity)
            print(f"{quantity} of {product.name} added to cart.")
        else:
            print(f"❌ Not enough stock for {product.name}.")

    def remove_item(self, pid):
        for item in self.items:
            if item.product.pid == pid:
                item.product.stock += item.quantity  # restore stock
                self.items.remove(item)
                print(f"{item.product.name} removed from cart.")
                return
        print("❌ Item not found in cart.")

    def view_cart(self):
        if not self.items:
            print("🛒 Cart is empty")
            return
        print("\n🛒 Items in Cart:")
        total = 0
        for item in self.items:
            price = item.display()
            print(f"{item.product.name} - Quantity: {item.quantity}, Price: ₹{price}")
            total += price
        print(f"💰 Total Price: ₹{total}")

    def checkout(self):
        if not self.items:
            print("🛒 Cart is empty. Cannot checkout.")
        else:
            self.view_cart()
            print("✅ Order placed successfully!")
            self.items.clear()


class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()


class ECommerceSystem:
    def __init__(self):
        self.products = [
            Product(1, "Phone", 15000, 10),
            Product(2, "Laptop", 60000, 5),
            Product(3, "Charger", 500, 20),
            Product(4, "Headphones", 1200, 15),
        ]
        self.user = User("Vaibhav")

    def display_products(self):
        print("\n📦 Available Products:")
        for product in self.products:
            product.display()

    def run(self):
        while True:
            print("\n==== E-Commerce Menu ====")
            print("1. View Products")
            print("2. Add to Cart")
            print("3. Remove from Cart")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_products()
            elif choice == '2':
                product_id = int(input("Enter Product ID to add to cart: "))
                quantity = int(input("Enter quantity: "))
                product = next((p for p in self.products if p.pid == product_id), None)
                if product:
                    self.user.cart.add_item(product, quantity)
                else:
                    print("❌ Product not found.")
            elif choice == '3':
                product_id = int(input("Enter Product ID to remove from cart: "))
                self.user.cart.remove_item(product_id)
            elif choice == '4':
                self.user.cart.view_cart()
            elif choice == '5':
                self.user.cart.checkout()
            elif choice == '6':
                print("👋 Thank you for shopping!")
                break
            else:
                print("❌ Invalid choice. Please try again.")


# Run the system
if __name__ == "__main__":
    system = ECommerceSystem()
    system.run()
