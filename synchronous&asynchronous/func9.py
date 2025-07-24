# check which is number is prime number or not ?
def is_prime(n):
    if n < 2:
        return f"Please Enter the above of 2 number"
    for i in range(2, n):
        if n % i == 0:
            return f"{n} - this number is not a Prime number"
    return f" {n} - number is a Prime Number"    


result = is_prime(1)
print(result)