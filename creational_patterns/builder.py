class SalesReport:
    def __init__(self):
        self.header = None
        self.body = None
        self.footer = None

    def display(self):
        print(self.header)
        print(self.body)
        print(self.footer)

class SalesReportBuilder:
    def __init__(self):
        self.report = SalesReport()

    def add_header(self):
        self.report.header = "=== SALES REPORT HEADER ==="
        return self

    def add_body(self):
        self.report.body = "Items Sold: 120 | Revenue: R5000"
        return self

    def add_footer(self):
        self.report.footer = "=== END OF REPORT ==="
        return self

    def build(self):
        return self.report
