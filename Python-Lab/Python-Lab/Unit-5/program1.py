# Program 1: Bank account using classes and objects

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Account Holder:", self.name)
        print("Balance       :", self.balance)


account = BankAccount("Akshaj Sharma", 5000)
account.deposit(2000)
account.withdraw(1500)
account.withdraw(10000)
account.display()
