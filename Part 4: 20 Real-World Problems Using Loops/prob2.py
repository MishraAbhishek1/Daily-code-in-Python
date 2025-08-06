# another way to solve problem 1 from user

cart_input = input("Enter the list of cart prices (comma-seperated, e.g, 10,20,30,40): ")

# here i convert input strings  conver in integers
cart = [int(price) for price in cart_input.split(",")]

# function to calculatte a total
def total_cart_price(cart):
    total=0
    for price in cart:
        total += price
    return total

print(F"Total Cart Price: ",total_cart_price(cart))

