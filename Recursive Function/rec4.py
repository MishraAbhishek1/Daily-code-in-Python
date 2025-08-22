# 🔹 Example 2: Fibonacci Series

def fibonacci_series(n):
    # BAse Case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive Case
    return fibonacci_series(n-1) + (n-2)

print(fibonacci_series(6))