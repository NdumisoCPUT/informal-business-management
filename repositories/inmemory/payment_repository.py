# repositories/inmemory/payment_repository.py

from src.payment import Payment

class InMemoryPaymentRepository:
    def __init__(self):
        self._payments = {}

    def add(self, payment: Payment):
        self._payments[payment.get_payment_id()] = payment

    def list_all(self):
        return list(self._payments.values())

    def find_by_id(self, payment_id: str):
        return self._payments.get(payment_id, None)

