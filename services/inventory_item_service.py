from src.inventory_item import InventoryItem
from repositories.inmemory.inventory_item_repository import InMemoryInventoryItemRepository

class InventoryItemService:
    def __init__(self, repository: InMemoryInventoryItemRepository):
        self.repository = repository

    def add_item(self, item: InventoryItem):
        return self.repository.add(item)  # Use 'add', not 'save'

    def list_items(self):
        return self.repository.list_all()  # Ensure method name matches repository

    def update_item(self, item_id: str, updated_item: InventoryItem):
        return self.repository.update(item_id, updated_item)

    def restock_item(self, item_id: str, quantity: int):
        return self.repository.restock(item_id, quantity)

    def mark_out_of_stock(self, item_id: str):
        return self.repository.mark_out_of_stock(item_id)
