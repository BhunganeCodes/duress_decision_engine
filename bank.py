# The Bank Class Where CBS Logic Will Be Found...

class Bank:
    def __init__(self, name: str):
        self.name = name

    def create_account(self):
        return f"Congratulations, new account created at {self.name}"

class Account(Bank):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit of R{amount} successfully deposited"

    def new_acc(self):
        return self.Bank.create_account()

absa = Bank("ABSA")
user1 = Account().new_acc()
print(user1)

fnb = Bank("FNB")
print(fnb.create_account())