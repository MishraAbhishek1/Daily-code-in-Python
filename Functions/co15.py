# 🔂 9. Function Inside Function (Nested Functions)
def outer():
    print("This is a Outer Function")

    def inner():
        print("This is a Inner Function")
    inner() 
outer()       