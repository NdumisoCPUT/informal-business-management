from repositories.sales_report_repository import SalesReportRepository
from src.sales_report import SalesReport

class DatabaseSalesReportRepository(SalesReportRepository):
    def save(self, entity: SalesReport) -> None:
        pass

    def find_by_id(self, id: int) -> SalesReport:
        pass

    def find_all(self) -> list[SalesReport]:
        pass

    def delete(self, id: int) -> None:
        pass
