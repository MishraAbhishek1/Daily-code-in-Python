# here we learn why we nested loops use problems
# first we understand why we use nested loops  in problems

orders = [
    {"order_id": 1, "items": [{"name": "Shirt", "price": 500}, {"name": "Jeans", "price": 1000}]},
    {"order_id": 2, "items": [{"name": "Shoes", "price": 2000}, {"name": "Socks", "price": 100}]}
]

#first loop
for order in orders:
    order_total = 0
    print(f"Order ID: {order['order_id']}")
    for item in order['items']:
        order_total +=  item['price']
        print(f"  Item: {item['name']}, Price: {item['price']}")
    print(f"  Order Total: {order_total}\n")