import unittest
from src.sales_report import SalesReport
from repositories.inmemory.sales_report_repository import InMemorySalesReportRepository
from services.sales_report_service import SalesReportService

class TestSalesReportService(unittest.TestCase):

    def setUp(self):
        self.repo = InMemorySalesReportRepository()
        self.service = SalesReportService(self.repo)

    def test_create_report(self):
        report = SalesReport("RPT001", "2024-01-01 to 2024-01-31", 10000.0, 250)
        output = self.service.create_report(report)

        self.assertIn("Sales Report RPT001", output)
        self.assertIn("Total Revenue: R10000.0", output)

    def test_export_report_success(self):
        report = SalesReport("RPT002", "2024-02-01 to 2024-02-28", 15000.0, 300)
        self.repo.add(report)

        result = self.service.export_report("RPT002")
