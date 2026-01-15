# This is the routing engine, not the decision maker
class TransactionSwitch:
    def __init__(self):
        self.banks = {}

    def register_bank(self, bank):
        self.banks[bank.name] = bank

    def route_transaction(self, transaction):
        bank = self.banks.get(transaction.bank_name)

        if not bank:
            return {
                "status": "DECLINED",
                "reason": "BANK_NOT_FOUND"
            }

        account = bank.accounts.get(transaction.account_number)

        if not account:
            return {
                "status": "DECLINED",
                "reason": "ACCOUNT_NOT_FOUND"
            }

        # Forward to CBS (duress-aware)
        return account.withdraw(
            entered_pin=transaction.entered_pin,
            requested_amount=transaction.requested_amount
        )
