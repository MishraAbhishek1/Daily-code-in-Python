# Write a Python program to swap two variables.

# > Here i take a two variable  for swapping
a = int(input("Enter the value of first a: "))
b = int(input("Enter the value of second b: "))

# Here i am display the origin al values

print(f"The original values of a = {a}, b = {b}")

# we do a swapping using a temp values
temp = a
a = b
b = temp

# display a swapped values
print(f" Swapped Values : a = {a}, b = {b}")