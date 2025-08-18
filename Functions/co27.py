# Python Global Variables

"""global variable  decalre in outside the fucntion we call in inside the
 function and also outside the fuction it is accessible in the whole programPython Global Variables
"""

# global variables

message = "Hello World!"

# create a function
def greet():
    # here we access a global Variable
    print("Global Variable acccess in the Function:", message)

greet()

# here we accesss a global cariable in outside the fucntion
print("Global Variable access in outside the Function:", message)

