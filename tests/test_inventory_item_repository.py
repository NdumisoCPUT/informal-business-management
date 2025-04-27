import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
from repositories.inmemory.inventory_item_repository import InMemoryInventoryItemRepository
from src.inventory_item import InventoryItem

class TestInventoryItemRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryInventoryItemRepository()
        self.item = InventoryItem(
            item_id="item-001",
            name="Sunlight Soap",
            quantity=50,
            price=15.0,
            restock_threshold=10
        )

    def test_save_and_find_by_id(self):
        self.repo.save(self.item)
        found_item = self.repo.find_by_id("item-001")
        self.assertIsNotNone(found_item)
        self.assertEqual(found_item.name, "Sunlight Soap")
        self.assertEqual(found_item.quantity, 50)

    def test_find_all(self):
        self.repo.save(self.item)
        all_items = self.repo.find_all()
        self.assertEqual(len(all_items), 1)

    def test_delete(self):
        self.repo.save(self.item)
        self.repo.delete("item-001")
        deleted_item = self.repo.find_by_id("item-001")
        self.assertIsNone(deleted_item)

if __name__ == '__main__':
    unittest.main()
