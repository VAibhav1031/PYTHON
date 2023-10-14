class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

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

class Review:
    def __init__(self, user, product, rating, comment):
        self.user = user
        self.product = product
        self.rating = rating
        self.comment = comment

class ECommerceSystem:
    def __init__(self):
        self.users = []
        self.products = []
        self.reviews = []

    def register_user(self, username, password):
        user = User(username, password)
        self.users.append(user)

    def write_review(self, username, product_name, rating, comment):
        user = next((u for u in self.users if u.username == username), None)
        product = next((p for p in self.products if p.name == product_name), None)
        if user and product:
            review = Review(user, product, rating, comment)
            self.reviews.append(review)

    def view_product_reviews(self, product_name):
        reviews = [r for r in self.reviews if r.product.name == product_name]
        if reviews:
            for review in reviews:
                print(f"User: {review.user.username}, Rating: {review.rating}")
                print(f"Comment: {review.comment}\n")
        else:
            print("No reviews for this product.")

class Order:
    def __init__(self, user_name, items):
        self.items = items
        self.user_name = user_name
        self.total_price = sum(product.price for product in self.items)

    def place_order(self):
        pay = input("How will you pay: Card, Online, UPI? ")
        
        if pay == "Card".lower():
            print("Swipe please! All Done")
            print("THANK YOU SIR\nVisit US Again")
        elif pay == "Online":
            print("All Done")
            print("THANK YOU SIR\nVisit US Again")
        elif pay == "UPI":
            print("Please Scan QR!!")
            print("THANK YOU SIR\nVisit US Again")

    def view_orders(self):
        print("Order details  for", self.user_name)
        for product in self.items:
            print(f"Product: {product.name}, Price: ${product.price}")
        print(f"Total Price: ${self.total_price}")

# Usage:

product1 = Product("TATA-Tea", 125, "250 gm", 100)
product2 = Product("Patanjali-Doodh-Biscuit", 40, "200 gm", 400)
product3 = Product("Patanjali-Honey", 380, "1 kg", 50)
product4 = Product("REfine", 215, "500 ml", 120)

shopp_ = ShoppingCart()

shopp_.add_product(product1)
shopp_.add_product(product2)
shopp_.add_product(product3)
shopp_.add_product(product4)

ecommerce = ECommerceSystem()
ecommerce.register_user("john_doe", "password123")
ecommerce.write_review("john_doe", "TATA-Tea", 5, "Excellent tea!")
ecommerce.write_review("john_doe", "Patanjali-Doodh-Biscuit", 4, "Tasty biscuits")
ecommerce.view_product_reviews("TATA-Tea")
ecommerce.view_product_reviews("Patanjali-Doodh-Biscuit")

shopp_ = ShoppingCart()
order_ = Order("vaibhav", shopp_.items)
order_.place_order()

order_.view_orders()
