# Variable Arguments  *args and  **kwargs
# simply we say args means Multiple Postoional Values
def total(*numbers):
    print(numbers)
    print(sum(numbers))
total(1,2,3,4)    