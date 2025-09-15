try:
    amount = int (input("Enter the amount: "))
    print("You entered: ", amount)
except Exception as e:
    print("Error: ", e)    