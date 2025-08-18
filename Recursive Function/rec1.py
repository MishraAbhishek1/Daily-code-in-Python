# Recursive function

def factorial(n):
    "Here i use recursive  funciton in python"

    if n == 0 or n == 1:
        return 1
    else:
        return (n * factorial(n-1))
print(factorial(5))    