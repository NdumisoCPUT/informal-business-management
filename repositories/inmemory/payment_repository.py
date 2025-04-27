

from src.payment import Payment

class InMemoryPaymentRepository:
    def __init__(self):
        self.payments = {}

    def add(self, payment):
        if isinstance(payment, Payment):
            self.payments[payment.get_payment_id()] = payment
        else:
            raise TypeError("Only Payment objects can be added.")

    def get(self, payment_id):
        return self.payments.get(payment_id)

    def remove(self, payment_id):
        if payment_id in self.payments:
            del self.payments[payment_id]

    def list_all(self):
        return list(self.payments.values())
