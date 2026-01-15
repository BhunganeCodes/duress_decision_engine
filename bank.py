# The Bank Class Where CBS Logic Will Be Found...
import uuid

class Bank:
    def __init__(self, name: str):
        self.name = name
        self.accounts = {}

    def create_account(self, owner_name: str, opening_balance: int = 0):
        account_number = str(uuid.uuid4())[:8]

        account = Account(
            bank_name=self.name,
            account_number=account_number,
            owner=owner_name,
            balance=opening_balance
        )

        self.accounts[account_number] = account

        return account
    
class Account:
    def __init__(self, bank_name: str, account_number: str, owner: str, balance: int = 0):
        self.bank_name = bank_name
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transaction_log = []

    def deposit(self, amount: int):
        self.balance += amount
        self.transaction_log.append(f"Deposit: R{amount}")
        return f"R{amount} deposited successfully"

    def withdraw(self, amount: int):
        if amount > self.balance:
            return "INSUFFICIENT_FUNDS"

        self.balance -= amount
        self.transaction_log.append(f"Withdrawal: R{amount}")
        return f"R{amount} withdrawn successfully"

absa = Bank("ABSA")

user1 = absa.create_account("Thamsanqa Hadebe", 1000)
print(user1.bank_name)
print(user1.account_number)
print(user1.deposit(500))
print(user1.withdraw(200))
print(user1.balance)