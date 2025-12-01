# # 🔶 1️⃣ Encapsulation – 10 Programs

# # ✔ Program 1 — Private Variable Access

# class Student:
#     def __init__(self, name):
#         self.__name = name
#         # self.__age = age

#     def get_name(self):
#         return self.__name
#         # return self.age
      

# s=Student("Abhishek")
# print(s.get_name())

# # ✔ Program 2 — Private + Setter Validation

# class Bank:
#     def __init__(self):
#         self.__balance=0

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
    
#     def get_balance(self):
#         return self.__balance
    
# b = Bank()
# b.deposit(500)
# print(b.get_balance())

# ✔ Program 3 — Protected Variable

class a:
    def __init__(self):
        self._value=10

class b(a):
    def show(self):
        print(self._value)

b().show()

# When we use a outside a class (protected vairable) Maintainblity is badd

# (_single underscore) define a protected varaible

class a:
    def __init__(self):
        self._value = 10

A = a()
print(A._value)

# when we wtite a __double underscore means a private variable

# class B:
#     def __init__(self):
#         self.__value = 20

# b = B()
# print(b.__value)

class Emplyoee:
    def __init__(self):
        self.__salary = 500

e = Emplyoee()
print(e._Emplyoee__salary)