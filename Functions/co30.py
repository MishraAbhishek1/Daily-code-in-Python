# c = 1
# def modify():
#     c = c + 1
#     print("Modified c:", c)
# modify()

# print("Final c: ", c)

# >>>>>>>>>>>>>>>>..
# global variable
c = 1 

def add():
    global c
     # increment c by 2
    c = c + 2

    print(c)

add()