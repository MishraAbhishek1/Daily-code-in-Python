# Python Object-Oriented Programming: Person class with age calculation

from datetime import datetime

# make a person class
class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.birth_year = birth_year
        self.country = country

    # here we make a calculate_age method this function will be calculated age
    def calculate_age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year
    
    # here we take input from users
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
country = input("Enbter your copuntry: ")
p = Person(name, country, birth_year)
age = p.calculate_age()
print(f"{p.name} is {age} year old")