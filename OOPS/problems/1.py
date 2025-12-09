# Python Object-Oriented Programming: Circle class with area and perimeter calculation

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    # calculate and return area of the circle using formulla
    def calculate_circle_of_area(self):
        return math.pi * self.radius**2

    # caluclate the return of parmaeter of the circle
    def calculate_circle_of_perimeter(self):
        return 2 * math.pi * self.radius


radius = float(input("Input the radious of the circle"))
circle = Circle(radius)
area = circle.calculate_circle_of_area()

perimeter = circle.calculate_circle_of_perimeter()

print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter)