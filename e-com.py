import random
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AuthSystem:
    def __init__(self):
        self.users = [User("vaibhav", "va78%1")]

    def authenticate(self, username, password):
        user = next((u for u in self.users if u.username == username), None)
        if user and user.password == password:
            return True
        return False


class Product:
    def __init__(self, name, price, description, quantity_in_stock):
        self.name = name
        self.price = price
        self.description = description
        self.quantity_in_stock = quantity_in_stock

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, name):
        for product in self.items:
            if product.name == name:
                self.items.remove(product)

    def calculate_total(self):
        total = sum(product.price for product in self.items)
        return total

class Order:
    def __init__(self, user_name, items):
        self.items = items
        self.user_name = user_name
        self.total_price = sum(product.price for product in self.items)

    def place_order(self):
        pay = input("How will you pay: Card, Online, UPI? ")
        
        if pay.lower() == "card":
            print("Swipe please! All Done")
            print("THANK YOU SIR\nVisit US Again")
        elif pay.lower() == "online":
            print("All Done")
            print("THANK YOU SIR\nVisit US Again")
        elif pay.lower() == "upi":
            print("Please Scan QR!!")
            print("THANK YOU SIR\nVisit US Again")

    def view_orders(self):
        bi = random.randint(1, 500)
        print("Bill no.",bi)
        print("Order details  for",self.user_name)
        for product in self.items:
            print(f"Product:{product.name},Price:${product.price}")
        print(f"Total Price:${self.total_price}")


auth_system = AuthSystem()     
while True:
    username = input("Enter the Username: ")
    password = input("Enter the Password: ")
    if auth_system.authenticate(username, password):
        print("Authentication Is Correct!")
        break
    else:
        print("Invalid Username or Password. Please try again.")

# Check if authentication was successful before proceeding
if auth_system.authenticate(username, password):
    product1 = Product("TATA-Tea", 125, "250 gm", 100)
    product2 = Product("Patanjali-Doodh-Biscuit", 40, "200 gm", 400)
    product3 = Product("Patanjali-Honey", 380, "1 kg", 50)
    product4 = Product("REfine", 215, "500 ml", 120)

    shopp_ = ShoppingCart()

    shopp_.add_product(product1)
    shopp_.add_product(product2)
    shopp_.add_product(product3)
    shopp_.add_product(product4)

    order_ = Order(username, shopp_.items)
    order_.place_order()

    order_.view_orders()
else:
    print("Authentication failed. Access denied.")