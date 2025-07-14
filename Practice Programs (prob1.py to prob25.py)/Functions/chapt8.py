## without *args (Normal Way)
def add(a,b):
    return a+b
print(add(1,2))
# print(add(1,2,3)) # this line through error too many arguments
'''This is the main reason we use args  with the help of we use a multiple arguments'''
import math
# >>>>>>>>>>>>>>>>>>>> using args >>>>>>>>>>>>>>>>....
def add_all(*num):
    print(num)
    print(sum(num))
    print(math.prod(num))
x = add_all(1,2,3,4)
print(x)