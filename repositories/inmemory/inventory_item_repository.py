from typing import Optional, List
from repositories.inventory_item_repository import InventoryItemRepository
from src.inventory_item import InventoryItem

class InMemoryInventoryItemRepository(InventoryItemRepository):
    def __init__(self):
        self._storage = {}

    def save(self, item: InventoryItem) -> None:
        self._storage[item.id] = item

    def find_by_id(self, id: str) -> Optional[InventoryItem]:
        return self._storage.get(id)

    def find_all(self) -> List[InventoryItem]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        self._storage.pop(id, None)
