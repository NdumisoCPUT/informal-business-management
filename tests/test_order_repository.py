# tests/test_order_repository.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
from repositories.inmemory.order_repository import InMemoryOrderRepository
from src.order import Order
from src.inventory_item import InventoryItem

class TestInMemoryOrderRepository(unittest.TestCase):

    def setUp(self):
        self.repo = InMemoryOrderRepository()
        self.order = Order(order_id=1, status="Pending", date_created="2024-04-26", total_amount=0)
        self.item = InventoryItem(
            item_id=101,
            name="Laptop",
            price=15000,
            quantity=5,
            restock_threshold=2
        )
        self.order.add_item(self.item)

    def test_add_and_get_order(self):
        self.repo.add(self.order)
        retrieved_order = self.repo.get(1)
        self.assertIsNotNone(retrieved_order)
        self.assertEqual(retrieved_order._Order__order_id, 1)

    def test_remove_order(self):
        self.repo.add(self.order)
        self.repo.remove(1)
        self.assertIsNone(self.repo.get(1))

    def test_list_all_orders(self):
        self.repo.add(self.order)
        orders = self.repo.list_all()
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0]._Order__order_id, 1)

if __name__ == "__main__":
    unittest.main()
