# Python Nonlocal Variables

#outerfunction 

def outer_function():
    #here i create a  nonlocal Variable
    message = "Hello from a Outer Function!"

    # this is a nested Function
    def inner_function():
        # here we access a nonlocal variables
        nonlocal message
        print("NonLocal Variable access in the Innenr Function:", message)

    inner_function()
    print("outer Function:", message)
outer_function()