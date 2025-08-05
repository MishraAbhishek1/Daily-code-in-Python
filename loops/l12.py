# 5. Looping with enumerate
# enumerate provides both index and value when iterating.


# Example 7: Indexing Items

items = ['apple', 'banana', 'pineapple']
for index, item in enumerate(items):
    print(f"Item {index+0}: {item}")