# ✅ Problem 7: Order Quantity Validation

quantity = int(input("Enter the quantity of products you want to order: "))

#applying condition >>

if quantity <= 0:
    print("Invalid quantiy .Please eneter a posititve number.")
elif quantity > 100:
    print("Order Quanttity is  Exceeded. Please reduce the quantity.")
else:
    print(f"Your order for {quantity} products has been placed successfully.")        