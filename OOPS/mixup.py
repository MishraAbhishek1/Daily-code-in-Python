# 🔶 1️⃣ Encapsulation – 10 Programs

# ✔ Program 1 — Private Variable Access

class Student:
    def __init__(self, name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
        # return self.age
      

s=Student("Abhishek")
print(s.get_name())