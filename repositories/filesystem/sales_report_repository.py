# repositories/filesystem/sales_report_repository.py

import os
import json
from src.sales_report import SalesReport

class FileSystemSalesReportRepository:
    def __init__(self, storage_dir="data/sales_reports"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def _get_report_filepath(self, report_id):
        return os.path.join(self.storage_dir, f"sales_report_{report_id}.json")

    def add(self, report):
        if not isinstance(report, SalesReport):
            raise TypeError("Only SalesReport objects can be added.")

        filepath = self._get_report_filepath(report.get_report_id())
        with open(filepath, 'w') as f:
            json.dump({
                "report_id": report.get_report_id(),
                "date_range": report.get_date_range(),
                "total_revenue": report.get_total_revenue(),
                "items_sold": report.get_items_sold()
            }, f, indent=4)

    def get(self, report_id):
        filepath = self._get_report_filepath(report_id)
        if not os.path.exists(filepath):
            return None

        with open(filepath, 'r') as f:
            data = json.load(f)
            report = SalesReport(
                report_id=data["report_id"],
                date_range=data["date_range"],
                total_revenue=data["total_revenue"],
                items_sold=data["items_sold"]
            )
            return report

    def remove(self, report_id):
        filepath = self._get_report_filepath(report_id)
        if os.path.exists(filepath):
            os.remove(filepath)

    def list_all(self):
        reports = []
        for filename in os.listdir(self.storage_dir):
            if filename.startswith("sales_report_") and filename.endswith(".json"):
                report_id = int(filename.replace("sales_report_", "").replace(".json", ""))
                report = self.get(report_id)
                if report:
                    reports.append(report)
        return reports
