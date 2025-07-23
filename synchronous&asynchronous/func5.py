def even_odd_finder(n):
    if n > 0:
        if n % 2 == 0:
            return "This number is Even"
        else:
            return "This number is Odd"
    else:
        return "Please enter a positive number"

result = even_odd_finder(-1)
print(result)
