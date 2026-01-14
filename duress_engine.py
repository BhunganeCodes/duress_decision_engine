# Duress Decision Engine Logic Concept Simplistic Version.

class DuressDecisionEngine:

    def __init__(self):
        pass

    def risk_analysis(self, pin, requested_amount):
        duress_pin = int(str(pin)[::-1])

        if pin == duress_pin:
            response = {
                "approved": True,
                "dispense_amount": 200,
                "silent_alert": True,
                "flag": "DURESS_EVENT"
            }
        else:
            response = {
                "approved": True,
                "dispense_amount": requested_amount,
                "silent_alert": False
            }
        return response
