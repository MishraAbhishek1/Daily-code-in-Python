# 1. User Input Conversion (Type Error Handling)

try:
    user = int(input("Enter the numbers: "))
    print("You entered: ", user)
# except Exception as e:
except ValueError as e:
    print("Error: ", e)    