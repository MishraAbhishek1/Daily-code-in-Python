# 5. Division by Zero

try:

    x = int(input("Enter a number : "))
    y = int(input("Enter a number : "))
    print("Division : ", x/y)
except ZeroDivisionError as e:
    print("Error: ", e)    