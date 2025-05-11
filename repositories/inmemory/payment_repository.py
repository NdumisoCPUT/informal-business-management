from src.payment import Payment

class InMemoryPaymentRepository:
    def __init__(self):
        self._payments = {}

    def add(self, payment: Payment):
        self._payments[payment.get_payment_id()] = payment

    def save(self, payment: Payment):
        # Alias for add to satisfy service/tests
        return self.add(payment)

    def get(self, payment_id: str):
        # Alias for find_by_id
        return self.find_by_id(payment_id)

    def find_by_id(self, payment_id: str):
        return self._payments.get(payment_id, None)

    def remove(self, payment_id: str):
        return self._payments.pop(payment_id, None)

    def list_all(self):
        return list(self._payments.values())

