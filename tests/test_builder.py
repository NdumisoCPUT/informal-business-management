import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from creational_patterns.builder import SalesReportBuilder

def test_builder_creates_full_report():
    builder = SalesReportBuilder()
    report = builder.add_header().add_body().add_footer().build()
    assert report.header.startswith("===")
    assert "Items Sold" in report.body
    assert report.footer.endswith("===")
