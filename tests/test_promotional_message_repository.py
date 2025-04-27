# tests/test_promotional_message_repository.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
from repositories.inmemory.promotional_message_repository import InMemoryPromotionalMessageRepository
from src.promotional_message import PromotionalMessage

class TestInMemoryPromotionalMessageRepository(unittest.TestCase):

    def setUp(self):
        self.repo = InMemoryPromotionalMessageRepository()
        self.message = PromotionalMessage(
            message_id=1,
            content="Sale: 20% off all items!",
            channel="WhatsApp",
            target_group="All Customers",
            sent_date="2024-04-27"
        )

    def test_add_and_get_message(self):
        self.repo.add(self.message)
        retrieved_message = self.repo.get(1)
        self.assertIsNotNone(retrieved_message)
        self.assertEqual(retrieved_message._PromotionalMessage__content, "Sale: 20% off all items!")

    def test_remove_message(self):
        self.repo.add(self.message)
        self.repo.remove(1)
        self.assertIsNone(self.repo.get(1))

    def test_list_all_messages(self):
        self.repo.add(self.message)
        messages = self.repo.list_all()
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]._PromotionalMessage__message_id, 1)

if __name__ == "__main__":
    unittest.main()
