# repositories/inmemory/sales_report_repository.py

from src.sales_report import SalesReport

class InMemorySalesReportRepository:
    def __init__(self):
        self.reports = {}

    def add(self, report):
        if isinstance(report, SalesReport):
            self.reports[report.get_report_id()] = report
        else:
            raise TypeError("Only SalesReport objects can be added.")

    def get(self, report_id):
        return self.reports.get(report_id)

    def remove(self, report_id):
        if report_id in self.reports:
            del self.reports[report_id]

    def list_all(self):
        return list(self.reports.values())
