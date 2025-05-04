import unittest
from services.order_service import OrderService
from repositories.inmemory.order_repository import InMemoryOrderRepository
from src.order import Order
from src.inventory_item import InventoryItem

class TestOrderService(unittest.TestCase):
    def test_order_service(self):
        repo = InMemoryOrderRepository()
        service = OrderService(repo)

        item = InventoryItem("ITEM001", "Bread", 2, 15.0, 5)
        order = Order("ORDER001", "Pending", "2024-05-01", 0.0)
        order.add_item(item)
        order.calculate_total()

        service.submit_order(order)

        self.assertEqual(service.find_order("ORDER001").get_total_amount(), 30.0)
        self.assertTrue(service.cancel_order("ORDER001"))
        self.assertFalse(service.cancel_order("ORDER001"))  # Already cancelled

if __name__ == '__main__':
    unittest.main()

