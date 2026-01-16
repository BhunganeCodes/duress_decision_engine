# The Bank Class Where CBS Logic Will Be Found...
import uuid
from duress_engine import DuressDecisionEngine
import random
from datetime import datetime

class BankCard:
    cards_issued = set()

    def __init__(self):
        self.card_number = self.generate_number()
        self.expiry_date = self.generate_expiry_date()
        # self.cvv = cvv
    
    def generate_number(self):
        number = "".join(str(random.randint(0, 9)) for _ in range(16))

        while True:
            if number not in BankCard.cards_issued:
                BankCard.cards_issued.add(number)
                return number
    
    def generate_expiry_date(self):
        current_year = datetime.now().year
        current_month = datetime.now().month

        expiry_year = current_year + random.randint(3, 5)
        expiry_month = random.randint(1, 12)

        return f"{expiry_month:02d}/{str(expiry_year)[-2:]}"


class Bank:
    def __init__(self, name: str):
        self.name = name
        self.accounts = {}

    def create_account(self, owner_name: str, pin: int, opening_balance: int = 0):
        account_number = str(uuid.uuid4())[:8]

        account = Account(
            bank_name=self.name,
            account_number=account_number,
            owner=owner_name,
            pin=pin,
            balance=opening_balance
        )

        self.accounts[account_number] = account
        return account

class Account:
    def __init__(
        self,
        bank_name: str,
        account_number: str,
        owner: str,
        pin: int,
        balance: int = 0
    ):
        self.bank_name = bank_name
        self.account_number = account_number
        self.owner = owner
        self.pin = pin
        self.balance = balance
        self.transaction_log = []
        self.duress_log = []

        # Each account has its own duress engine
        self.duress_engine = DuressDecisionEngine(primary_pin=pin)


    def deposit(self, amount: int):
        self.balance += amount
        self.transaction_log.append(f"Deposit: R{amount}")
        return f"R{amount} deposited successfully"

    def withdraw(self, entered_pin: int, requested_amount: int):
        decision = self.duress_engine.analyze(
            entered_pin=entered_pin,
            requested_amount=requested_amount
        )

        if not decision.get("approved"):
            return {
                "status": "DECLINED",
                "reason": decision.get("reason")
            }

        dispense_amount = decision["dispense_amount"]

        if dispense_amount > self.balance:
            return {
                "status": "DECLINED",
                "reason": "INSUFFICIENT_FUNDS"
            }

        # CBS executes the withdrawal
        self.balance -= dispense_amount
        self.transaction_log.append(
            f"Withdrawal: R{dispense_amount}"
        )

        if decision.get("silent_alert"):
            self.duress_log.append({
                "event": "DURESS_EVENT",
                "amount_requested": requested_amount,
                "amount_dispensed": dispense_amount
            })

        return {
            "status": "APPROVED",
            "dispensed": dispense_amount,
            "silent_alert": decision.get("silent_alert", False)
        }

# Test Simulation of the duress engine
absa = Bank("ABSA")

user = absa.create_account(
    owner_name="Thamsanqa Hadebe",
    pin=1234,
    opening_balance=1000
)

# Normal withdrawal
print(user.withdraw(entered_pin=1234, requested_amount=500))

# Duress withdrawal
print(user.withdraw(entered_pin=4321, requested_amount=1000))

# Invalid PIN
print(user.withdraw(entered_pin=1111, requested_amount=100))
