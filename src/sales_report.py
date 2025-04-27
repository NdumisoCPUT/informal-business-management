# src/sales_report.py

class SalesReport:
    def __init__(self, report_id, date_range, total_revenue, items_sold):
        self.__report_id = report_id
        self.__date_range = date_range
        self.__total_revenue = total_revenue
        self.__items_sold = items_sold

    def generate(self):
        return (f"Sales Report {self.__report_id}\n"
                f"Date Range: {self.__date_range}\n"
                f"Total Revenue: R{self.__total_revenue}\n"
                f"Total Items Sold: {self.__items_sold}")

    def export(self):
        print(f"Exporting Sales Report {self.__report_id} for {self.__date_range}...")

    def save_to_history(self):
        print(f"Sales Report {self.__report_id} has been saved to history.")

    # Getter methods for clean access (good practice)
    def get_report_id(self):
        return self.__report_id

    def get_date_range(self):
        return self.__date_range

    def get_total_revenue(self):
        return self.__total_revenue

    def get_items_sold(self):
        return self.__items_sold

