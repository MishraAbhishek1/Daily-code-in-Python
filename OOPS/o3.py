# 🧩 Program 1: Class and Object (Real-World Example)
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def show(self):
        print(f"{self.year} {self.make} {self.model}")

c1 = Car("Honda", "Civic", 2020)
c1.show()
       