# 🏦 4. Bank Account System
# 🧱 Static Way

class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")
    
acc = BankAccount("Abhishek", 5000)
acc.deposit(500)

# 💬 Dynamic Way
class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
    
    def deposit_ammount(self, amount):
        self.balance += amount
        print(f" Account Holer: {self.holder} \n Deposited Money: {amount}, New balance: {self.balance}")

# dynamic value
holder =  input("Enter your name: ")
balance = int(input("Enter your balance"))
amount = int(input("Enter your amount yo add in this account: "))

b = BankAccount(holder, balance)
b.deposit_ammount(amount)