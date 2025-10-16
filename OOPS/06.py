# 🧩 Program 3: Abstraction (Hiding Implementation Details)

from abc import ABC, abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class Paypal(PaymentGateway):
    def make_payment(self, amount):
        print(f"Paid {amount} using paypal")

payment = Paypal()
payment.make_payment(100)        
