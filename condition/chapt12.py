#First Problem: Positive, Negative, or Zero
try:
    num = int(input("Enter a number: "))
    if num >= 0:
        print("The number is positive or zero")
    elif num <0:
        print("The Number is negative")
    else:
        print("This is not a valid number")   
except ValueError:
    print("Invalid input. Please enter a Valid integer! ")     