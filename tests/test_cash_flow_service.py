import unittest
from datetime import datetime
from src.cash_flow_entry import CashFlowEntry
from repositories.inmemory.cash_flow_entry_repository import InMemoryCashFlowEntryRepository
from services.cash_flow_entry_service import CashFlowService

class TestCashFlowService(unittest.TestCase):

    def setUp(self):
        self.repo = InMemoryCashFlowEntryRepository()
        self.service = CashFlowService(self.repo)

    def test_add_valid_income_entry(self):
        entry = CashFlowEntry("CF001", 500.0, "income", "active", datetime.now())
        added = self.service.add_entry(entry)

        self.assertEqual(added.get_entry_id(), "CF001")
        self.assertEqual(added.get_type(), "income")
        self.assertEqual(added.get_status(), "active")

    def test_add_invalid_entry_raises(self):
        entry = CashFlowEntry("CF002", -100.0, "income", "active", datetime.now())
        with self.assertRaises(ValueError):
            self.service.add_entry(entry)

    def test_archive_entry(self):
        entry = CashFlowEntry("CF003", 250.0, "expense", "active", datetime.now())
        self.repo.add(entry)

        archived = self.service.archive_entry("CF003")
        self.assertEqual(archived.get_status(), "archived")

    def test_get_entry(self):
        entry = CashFlowEntry("CF004", 1000.0, "income", "active", datetime.now())
        self.repo.add(entry)

        result = self.service.get_entry("CF004")
        self.assertIsNotNone(result)
        self.assertEqual(result.get_amount(), 1000.0)

    def test_list_entries(self):
        entry1 = CashFlowEntry("CF005", 300.0, "income", "active", datetime.now())
        entry2 = CashFlowEntry("CF006", 150.0, "expense", "active", datetime.now())
        self.repo.add(entry1)
        self.repo.add(entry2)

        all_entries = self.service.list_entries()
        self.assertEqual(len(all_entries), 2)

if __name__ == '__main__':
    unittest.main()
