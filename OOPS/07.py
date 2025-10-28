'''
🧩 Problem before OOP (Old Way — Procedural Programming)

Python (aur purani languages jaise C) me pehle hum code likhte the procedural way me —
yaani sab functions alag-alag likh dete the, aur data (variables) bhi alag rakhte the.

Example:
'''

# procedural way to write  a program
name = "Abhishek"
age = 22

def show_details():
    print(f"Name: {name}, Age: {age}")

show_details()

'''Agar tumhare paas 100 log hote to kya hota?
👉 Har ek ke liye name, age, aur function likhne padte — code messy ho jata, aur reusability khatam.'''


# every thing in real world is a Object and class have a object like assume my complany  is a class and in employee is a object
# we design a code like real world 

'''
🚀 Solution: Object-Oriented Programming (OOP)

OOP ka main idea yeh hai:

“Code ko real-world objects jaise design karo — har object ke apne data (attributes) aur apne actions (methods) hote hain.”

Matlab:

Har real-world cheez ko ek object ke roop me treat karo.

Object ek class se banta hai.

Class ek blueprint hai (jaise ghar banane ka naksha).

Object us class ka instance hota hai (real ghar).
'''

# without oops

name1 = "Abhishek"
age1 = 22
rollno1 = 122

name2 = "Rahul"
age2 = 23
rollno2 = 123

# this is line of code repeat its not good here we use a class  reduce code redabillity

# with OOP

class Student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        print("Constructor Called!")
    
    def show_details(self):
        print(f"Name:{self.name},Age:{self.age},Roll_no:{self.roll_no}")

# create Objects
s1 = Student("Abhishek", 22, 212)
s2 = Student("ravi", 23, 2122)

s1.show_details()
s2.show_details()