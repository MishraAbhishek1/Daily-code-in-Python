# ✅ Problem 23: Discount Based on Amount

amount = int(input("Enter the bill amount: "))

if amount  >= 1000:
    print("%20 Discount")
elif amount >= 5000:
    print("10% Discount")
else:
    print("No Discount")        