# Generate Invoice (E-commerce)

products = {"laptop":1000, "Mouse":200, "Keyboard":1000}

for item, price in products.items():
    print(f"{item}: ${price}")
print(f"Total : ${sum(products.values())}")    