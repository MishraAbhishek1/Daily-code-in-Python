'''
Why oops is Needed ?
problem is code repetion : How to be solve like with the help of oops like use calsses and reuse them again and agin

'''

# 🧩 1. Student Management System (Basic Class & Object)

# 🧱 Static Way

class Student:
    def __init__(self, name, roll, course):
        self.name = name
        self.roll = roll
        self.course = course

    def show_deatils(self):
        print(f"Name: {self.name}, Roll_No: {self.roll}, course: {self.course}")

# Static object
s1 = Student("Abhishek", 2121932, "AI&ML")
s1.show_deatils()

# 💬 Dynamic Way

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Dynmaic here we input get from a user
name = input("Enter name: ")
age = int(input("Enter roll number: "))

s = Student(name, age)
s.show_details()
