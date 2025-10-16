# class myclass():
#     print("This is a class")

class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

e1 = employee("john", 23)
print(f"{e1.name}, {e1.age}")        