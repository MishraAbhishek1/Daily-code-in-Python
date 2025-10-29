# 🏫 6. Teacher & Student (Relationship Example)
# 🧱 Static Way

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    
class Student:
    def __init__(self, name):
        self.name = name

# hardcoded input
t = Teacher("Priya", "Maths")
s = Student("Abhishek")

print(f"{s.name} is taught by {t.name} ")