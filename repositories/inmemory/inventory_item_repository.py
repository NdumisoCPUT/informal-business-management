from src.inventory_item import InventoryItem

class InMemoryInventoryItemRepository:
    def __init__(self):
        self._storage = {}

    def add(self, item: InventoryItem):
        self._storage[item.get_item_id()] = item
        return item

    def save(self, item: InventoryItem):  # <--- Added this method for tests
        return self.add(item)

    def find_by_id(self, item_id: str):
        return self._storage.get(item_id)

    def list_all(self):
        return list(self._storage.values())

    def delete(self, item_id: str):
        return self._storage.pop(item_id, None)

    def update(self, item_id: str, updated_item: InventoryItem):
        if item_id in self._storage:
            self._storage[item_id] = updated_item
            return updated_item
        return None

    def restock(self, item_id: str, quantity: int):
        item = self._storage.get(item_id)
        if item:
            item.set_quantity(item.get_quantity() + quantity)
            return item
        return None

    def mark_out_of_stock(self, item_id: str):
        item = self._storage.get(item_id)
        if item:
            item.set_status("out_of_stock")
            return item
        return None
