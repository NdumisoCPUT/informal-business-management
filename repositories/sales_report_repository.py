# repositories/sales_report_repository.py

from repositories.repository import Repository
from src.sales_report import SalesReport

class SalesReportRepository(Repository[SalesReport, int]):
    pass
