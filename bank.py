# The Bank Class Where CBS Logic Will Be Found...

class Bank:
    def __init__(self, name: str):
        self.name = name

    def create_account(self):
        return f"Congratulations, new account created at {self.name}"

class Account(Bank):
    def __init__(self):
        ...

    def new_acc(self):
        return Bank.create_account()

absa = Bank("ABSA")
print(absa.create_account())

fnb = Bank("FNB")
print(fnb.create_account())