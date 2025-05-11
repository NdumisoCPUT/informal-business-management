import sys
import os
from datetime import datetime
import unittest

# Ensure src is in the import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from repositories.inmemory.payment_repository import InMemoryPaymentRepository
from src.payment import Payment

class TestInMemoryPaymentRepository(unittest.TestCase):

    def setUp(self):
        self.repo = InMemoryPaymentRepository()
        self.payment = Payment(
            payment_id="1",
            amount=250.0,
            method="Card",
            status="Pending",
            date=datetime(2024, 4, 27)  # ✅ FIXED: match constructor
        )

    def test_add_and_get_payment(self):
        self.repo.add(self.payment)
        retrieved_payment = self.repo.get("1")
        self.assertIsNotNone(retrieved_payment)
        self.assertEqual(retrieved_payment.get_amount(), 250.0)

    def test_remove_payment(self):
        self.repo.add(self.payment)
        self.repo.remove("1")
        self.assertIsNone(self.repo.get("1"))

    def test_list_all_payments(self):
        self.repo.add(self.payment)
        payments = self.repo.list_all()
        self.assertEqual(len(payments), 1)
        self.assertEqual(payments[0].get_payment_id(), "1")

if __name__ == "__main__":
    unittest.main()
