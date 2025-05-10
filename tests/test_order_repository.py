import unittest
from src.order import Order
from repositories.inmemory.order_repository import InMemoryOrderRepository

class TestInMemoryOrderRepository(unittest.TestCase):

    def test_add_and_get_order(self):
        repo = InMemoryOrderRepository()
        order = Order("ORD001", "Pending", "2024-01-01", 0.0)
        repo.add_order(order)

        fetched = repo.get_order("ORD001")
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.get_order_id(), "ORD001")
        self.assertEqual(fetched.get_status(), "Pending")

    def test_list_all_orders(self):
        repo = InMemoryOrderRepository()
        order1 = Order("ORD001", "Pending", "2024-01-01")
        order2 = Order("ORD002", "Completed", "2024-01-02")
        repo.add_order(order1)
        repo.add_order(order2)

        all_orders = repo.list_orders()
        self.assertEqual(len(all_orders), 2)
        self.assertIn(order1, all_orders)
        self.assertIn(order2, all_orders)

    def test_remove_order(self):
        repo = InMemoryOrderRepository()
        order = Order("ORD001", "Pending", "2024-01-01")
        repo.add_order(order)
        repo.remove_order("ORD001")
        self.assertIsNone(repo.get_order("ORD001"))

if __name__ == '__main__':
    unittest.main()
