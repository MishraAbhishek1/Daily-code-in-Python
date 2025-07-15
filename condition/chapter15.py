# ✅ Problem 4: Payment Status Checker

status = input("Enter your Payement Status ): ").upper()

if status == "PAID":
    print("Your payment is Successful! ")
elif status == "PENDING":
    print("Your payment is still pending. Please Wait!")
elif status == "FAILED":
    print("Your payment has Failed. Please try again")
else:
    print("Invalid status entered. Please check your input. ")            