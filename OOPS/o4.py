# 🧩 Program 2: Encapsulation (Private Data Protection)

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
        