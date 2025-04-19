class SalesReport:
    def __init__(self, report_id, date_range, total_revenue, items_sold):
        self.__report_id = report_id
        self.__date_range = date_range
        self.__total_revenue = total_revenue
        self.__items_sold = items_sold  

    def generate(self):
       
        return f"Report {self.__report_id} for {self.__date_range}: R{self.__total_revenue}, {self.__items_sold} items sold"

    def export(self):
       
        print("Exporting report...")

    def save_to_history(self):
        
        print("Report saved to history.")
