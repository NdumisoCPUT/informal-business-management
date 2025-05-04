import unittest
from datetime import datetime
from src.payment import Payment
from repositories.inmemory.payment_repository import InMemoryPaymentRepository
from services.payment_service import PaymentService

class TestPaymentService(unittest.TestCase):

    def setUp(self):
        self.repo = InMemoryPaymentRepository()
        self.service = PaymentService(self.repo)

    def test_process_payment_successful(self):
        payment = Payment("P001", 150.0, "Card", "Pending", datetime.now())
        self.repo.save(payment)

        processed = self.service.process_payment("P001")
        self.assertEqual(processed.get_status(), "Completed")

    def test_process_payment_failure(self):
        payment = Payment("P002", 0.0, "Card", "Pending", datetime.now())  # invalid amount
        self.repo.save(payment)

        processed = self.service.process_payment("P002")
        self.assertEqual(processed.get_status(), "Failed")

    def test_retry_payment(self):
        # Initially fail
        payment = Payment("P003", 0.0, "EFT", "Pending", datetime.now())
        self.repo.save(payment)
        self.service.process_payment("P003")

        # Manually correct the amount before retrying
        payment._Payment__amount = 50.0  # not ideal, but needed for testing private fields

        retried = self.service.retry_payment("P003")
        self.assertEqual(retried.get_status(), "Completed")

    def test_process_nonexistent_payment_raises(self):
        with self.assertRaises(ValueError) as context:
            self.service.process_payment("INVALID_ID")
        self.assertEqual(str(context.exception), "Payment not found")

    def test_get_payment(self):
        payment = Payment("P004", 75.0, "Cash", "Pending", datetime.now())
        self.repo.save(payment)

        retrieved = self.service.get_payment("P004")
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.get_payment_id(), "P004")

if __name__ == '__main__':
    unittest.main()
