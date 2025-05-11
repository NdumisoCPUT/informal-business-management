import unittest
from src.order import Order
from repositories.inmemory.order_repository import InMemoryOrderRepository

class TestInMemoryOrderRepository(unittest.TestCase):

    def test_add_and_get_order(self):
        # Arrange
        repo = InMemoryOrderRepository()
        order = Order("ORD001", "Pending", "2024-01-01", 0.0)
        
        # Act
        repo.save(order)
        fetched = repo.find_by_id("ORD001")
        
        # Assert
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.get_order_id(), "ORD001")
        self.assertEqual(fetched.get_status(), "Pending")

    def test_list_all_orders(self):
        # Arrange
        repo = InMemoryOrderRepository()
        order1 = Order("ORD001", "Pending", "2024-01-01")
        order2 = Order("ORD002", "Completed", "2024-01-02")
        
        # Act
        repo.save(order1)
        repo.save(order2)
        all_orders = repo.list_all()
        
        # Assert
        self.assertEqual(len(all_orders), 2)
        self.assertIn(order1, all_orders)
        self.assertIn(order2, all_orders)

    def test_remove_order(self):
        # Arrange
        repo = InMemoryOrderRepository()
        order = Order("ORD001", "Pending", "2024-01-01")
        
        # Act
        repo.save(order)
        repo.delete("ORD001")
        deleted = repo.find_by_id("ORD001")
        
        # Assert
        self.assertIsNone(deleted)

if __name__ == '__main__':
    unittest.main()
