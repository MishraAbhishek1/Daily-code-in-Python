# 🚗 2. Car Showroom Management (Encapsulation)

# 🧱 Static Way

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def details(self):
        print(f"Car: {self.brand} {self.model} | Price: {self.price}")

c1 = Car("Tesla", "Model s", 51694894)
c1.details()

# 💬 Dynamic Way

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def show_info(self):
        print(f"Car: {self.brand} {self.model}, {self.price}")

brand = input("Enter the name of card: ")
model = input("Enter the Car Model: ")
price = int(input("Enter the Car Price: "))

c = Car(brand, model, price)
c.show_info()