# 🧩 Program 2: Encapsulation (Private Data Protection)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print("Direct Access to Balance:", account.get_balance())
# print("Current Balance:", account.balance())  Here we use encapsulate method in class it mean we not access outside the class simople we do a private a object its essential means