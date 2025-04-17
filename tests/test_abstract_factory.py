import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from creational_patterns.abstract_factory import BakeryFactory, BeverageFactory

def test_bakery_factory_creates_bread():
    bakery = BakeryFactory()
    item = bakery.create_item()
    assert item.__class__.__name__ == "Bread"

def test_beverage_factory_creates_juice():
    beverage = BeverageFactory()
    item = beverage.create_item()
    assert item.__class__.__name__ == "Juice"
