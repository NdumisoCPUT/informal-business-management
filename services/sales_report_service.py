from repositories.inmemory.sales_report_repository import InMemorySalesReportRepository
from src.sales_report import SalesReport

class SalesReportService:
    def __init__(self, repository: InMemorySalesReportRepository):
        self.repository = repository

    def create_report(self, report: SalesReport):
        self.repository.add(report)
        return report.generate()

    def export_report(self, report_id: str):
        report = self.repository.get(report_id)
        if report:
            report.export()
            return True
        return False

    def archive_report(self, report_id: str):
        report = self.repository.get(report_id)
        if report:
            report.save_to_history()
            return True
        return False

    def get_report(self, report_id: str):
        return self.repository.get(report_id)

