import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from creational_patterns.prototype import Order, OrderPrototypeRegistry

def test_prototype_clones_order():
    original = Order("ORD1001", ["Sugar", "Coffee"])
    registry = OrderPrototypeRegistry()
    registry.register("template_order", original)

    clone = registry.clone("template_order")
    assert clone.order_id == "ORD1001"
    assert clone.items == ["Sugar", "Coffee"]
    assert clone is not original
