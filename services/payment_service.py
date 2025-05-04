# services/payment_service.py

from src.payment import Payment
from repositories.inmemory.payment_repository import InMemoryPaymentRepository

class PaymentService:
    def __init__(self, repository: InMemoryPaymentRepository):
        self.repository = repository

    def add_payment(self, payment: Payment):
        self.repository.add(payment)
        return payment

    def get_payment(self, payment_id: str):
        return self.repository.find_by_id(payment_id)

    def list_payments(self):
        return self.repository.list_all()

    def retry_payment(self, payment_id: str):
        payment = self.repository.find_by_id(payment_id)
        if payment:
            payment.retry()
            return payment
        return None
