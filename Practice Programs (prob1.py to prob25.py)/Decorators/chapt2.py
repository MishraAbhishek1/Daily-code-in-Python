# decorator function using @
def decorator_func(func):
    def wrapper():
        print("Hello")
        func()
        print("Good Morning")
    return wrapper

@decorator_func
def greet():
    print("Abhishek Mishra")
    return greet

greet()
    