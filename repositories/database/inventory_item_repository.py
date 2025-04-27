from repositories.inventory_item_repository import InventoryItemRepository
from src.inventory_item import InventoryItem

class DatabaseInventoryItemRepository(InventoryItemRepository):
    def save(self, entity: InventoryItem) -> None:
        pass

    def find_by_id(self, id: str) -> InventoryItem:
        pass

    def find_all(self) -> list[InventoryItem]:
        pass

    def delete(self, id: str) -> None:
        pass
