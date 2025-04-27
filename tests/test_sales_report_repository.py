# tests/test_sales_report_repository.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
from repositories.inmemory.sales_report_repository import InMemorySalesReportRepository
from src.sales_report import SalesReport

class TestInMemorySalesReportRepository(unittest.TestCase):

    def setUp(self):
        self.repo = InMemorySalesReportRepository()
        self.report = SalesReport(
            report_id=1,
            date_range="01-04-2024 to 30-04-2024",
            total_revenue=45000.00,
            items_sold=150
        )

    def test_add_and_get_report(self):
        self.repo.add(self.report)
        retrieved = self.repo.get(1)
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.get_total_revenue(), 45000.00)

    def test_remove_report(self):
        self.repo.add(self.report)
        self.repo.remove(1)
        self.assertIsNone(self.repo.get(1))

    def test_list_all_reports(self):
        self.repo.add(self.report)
        reports = self.repo.list_all()
        self.assertEqual(len(reports), 1)
        self.assertEqual(reports[0].get_report_id(), 1)

if __name__ == "__main__":
    unittest.main()
