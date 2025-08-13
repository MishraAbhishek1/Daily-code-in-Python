# Function Argument with Default Values

def add_numbers(num1=2, num2=3):
    return num1 + num2

print(F"Sum of default values: {add_numbers()}")

print(F"Sum of 5 and 10: {add_numbers(5, 10)}")

print(F"i give only one value: another value is default {add_numbers(num2=10)}")