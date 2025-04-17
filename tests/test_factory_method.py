import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from creational_patterns.factory_method import PaymentFactory

def test_factory_method_returns_card_processor():
    processor = PaymentFactory.get_processor("card")
    assert processor.__class__.__name__ == "CreditCardProcessor"

def test_factory_method_returns_paypal_processor():
    processor = PaymentFactory.get_processor("paypal")
    assert processor.__class__.__name__ == "PayPalProcessor"
