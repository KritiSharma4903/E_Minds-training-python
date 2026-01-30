class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited: ", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw: ", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Current balance:", self.balance)

acc = BankAccount("Kriti", 21000)

acc.deposit(25000)
acc.withdraw(12000)
acc.show_balance()