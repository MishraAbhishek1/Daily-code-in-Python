# 🛒 5. Shopping Cart System
# 🧱 Static Way

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_cart(self):
        print("Items in cart:", self.items)

c = Cart()
c.add_item("shoes")
c.add_item("T-shirt")
c.show_cart()

# Dynamic way

class Cart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)

    def show_cart(self):
        print("Items in cart:", self.items)

cart = Cart()
for _ in range(3):
    item = input("Add item: ")
    cart.add_item(item)
cart.show_cart()