# 💼 3. Employee Payroll System

# 🧱 Static Way

class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Employee name is : {self.name} Annual salary ctc: {self.salary * 12}")

e = Employee("Ayush", 25000)
e.show_info()

# 💬 Dynamic Way

class Bank_Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}, your anual CTC: {self.salary * 12}")
# dynamic input not harcode
name = input("Enter you Name: ")
salary = int(input("enter your salary: "))

be = Bank_Employee(name, salary)
be.show_info()
