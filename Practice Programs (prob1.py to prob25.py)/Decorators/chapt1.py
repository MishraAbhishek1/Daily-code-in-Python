# learning Decorators

def decorators_function(func):
    def wrapper():
        print("Before")
        func()
        print("after")
        func()
    return wrapper  

def say_hello():
    print("Hello")

# i manually add a decorator
new_function = decorators_function(say_hello)
new_function()    