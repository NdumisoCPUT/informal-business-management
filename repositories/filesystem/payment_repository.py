# repositories/filesystem/payment_repository.py

import os
import json
from src.payment import Payment

class FileSystemPaymentRepository:
    def __init__(self, storage_dir="data/payments"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def _get_payment_filepath(self, payment_id):
        return os.path.join(self.storage_dir, f"payment_{payment_id}.json")

    def add(self, payment):
        if not isinstance(payment, Payment):
            raise TypeError("Only Payment objects can be added.")

        filepath = self._get_payment_filepath(payment.get_payment_id())
        with open(filepath, 'w') as f:
            json.dump({
                "payment_id": payment.get_payment_id(),
                "amount": payment.get_amount(),
                "method": payment._Payment__method,
                "status": payment.get_status(),
                "timestamp": payment._Payment__timestamp
            }, f, indent=4)

    def get(self, payment_id):
        filepath = self._get_payment_filepath(payment_id)
        if not os.path.exists(filepath):
            return None

        with open(filepath, 'r') as f:
            data = json.load(f)
            payment = Payment(
                payment_id=data["payment_id"],
                amount=data["amount"],
                method=data["method"],
                status=data["status"],
                timestamp=data["timestamp"]
            )
            return payment

    def remove(self, payment_id):
        filepath = self._get_payment_filepath(payment_id)
        if os.path.exists(filepath):
            os.remove(filepath)

    def list_all(self):
        payments = []
        for filename in os.listdir(self.storage_dir):
            if filename.startswith("payment_") and filename.endswith(".json"):
                payment_id = int(filename.replace("payment_", "").replace(".json", ""))
                payment = self.get(payment_id)
                if payment:
                    payments.append(payment)
        return payments
