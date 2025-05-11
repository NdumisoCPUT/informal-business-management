import unittest
from services.inventory_item_service import InventoryItemService
from repositories.inmemory.inventory_item_repository import InMemoryInventoryItemRepository
from src.inventory_item import InventoryItem  

class TestInventoryItemService(unittest.TestCase):

    def test_inventory_item_service(self):
        repo = InMemoryInventoryItemRepository()
        service = InventoryItemService(repo)

       
        item = InventoryItem("ITEM001", "Milk", 10, 25.5, 5)

        service.add_item(item)
        self.assertEqual(service.get_item("ITEM001"), item)
        self.assertIn(item, service.list_items())

        service.delete_item("ITEM001")
        self.assertIsNone(service.get_item("ITEM001"))

if __name__ == '__main__':
    unittest.main()
