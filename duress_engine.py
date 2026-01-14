

class DuressDecisionEngine:

    def __init__(self):
        pass

    def risk_analysis(self, pin, duress_pin):
        if pin == duress_pin:
            return {
                "silent_alert": True,
                "decreased_balance": True,
                "status": "APPROVED"
            }