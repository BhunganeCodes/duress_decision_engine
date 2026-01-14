# Duress Decision Engine Logic Concept Simplistic Version.

class DuressDecisionEngine:
    def __init__(self, primary_pin: int):
        self.primary_pin = primary_pin
        self.duress_pin = int(str(primary_pin)[::-1])  # simple demo rule

    def risk_analysis(self, entered_pin: int, requested_amount: int):
        if entered_pin == self.duress_pin:
            return {
                "approved": True,
                "dispense_amount": 200,
                "silent_alert": True,
                "flag": "DURESS_EVENT"
            }

        if entered_pin == self.primary_pin:
            return {
                "approved": True,
                "dispense_amount": requested_amount,
                "silent_alert": False
            }

        return {
            "approved": False,
            "reason": "INVALID_PIN"
        }
