from abc import ABC, abstractmethod

# Base interface for processors
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Concrete implementations
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of R{amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of R{amount}")

# Factory Method to return processors
class PaymentFactory:
    @staticmethod
    def get_processor(method):
        if method == "card":
            return CreditCardProcessor()
        elif method == "paypal":
            return PayPalProcessor()
        else:
            raise ValueError("Unsupported payment method")

