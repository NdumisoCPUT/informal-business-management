# tests/test_cash_flow_entry_repository.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
from repositories.inmemory.cash_flow_entry_repository import InMemoryCashFlowEntryRepository
from src.cash_flow_entry import CashFlowEntry

class TestInMemoryCashFlowEntryRepository(unittest.TestCase):

    def setUp(self):
        self.repo = InMemoryCashFlowEntryRepository()
        self.entry = CashFlowEntry(
            entry_id=1,
            amount=1000.0,
            entry_type="income",
            status="active",
            date="2024-04-27"
        )

    def test_add_and_get_entry(self):
        self.repo.add(self.entry)
        retrieved = self.repo.get(1)
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.get_amount(), 1000.0)

    def test_remove_entry(self):
        self.repo.add(self.entry)
        self.repo.remove(1)
        self.assertIsNone(self.repo.get(1))

    def test_list_all_entries(self):
        self.repo.add(self.entry)
        entries = self.repo.list_all()
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].get_entry_id(), 1)

if __name__ == "__main__":
    unittest.main()
