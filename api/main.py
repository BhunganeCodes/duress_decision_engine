from fastapi import FastAPI
from pydantic import BaseModel
from transaction_switch import TransactionSwitch
from bank import Bank

app = FastAPI(title="ATM Transaction Switch")

switch = TransactionSwitch()

# Defining the transaction schema 
class ATMTransaction(BaseModel):
    bank_name: str
    account_number: str
    entered_pin: int
    requested_amount: int
    atm_id: str
    location: str

# Transaction Endpoint
@app.post("/atm/withdraw")
def atm_withdraw(transaction: ATMTransaction):
    response = switch.route_transaction(transaction)
    return response

# Testing
absa = Bank("ABSA")
user = absa.create_account(
    owner_name="Thamsanqa Hadebe",
    pin=1234,
    opening_balance=1000
)

print(switch.register_bank(absa))
