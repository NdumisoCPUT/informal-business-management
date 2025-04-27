from repositories.repository import Repository
from src.inventory_item import InventoryItem

class InventoryItemRepository(Repository[InventoryItem, str]):
    pass
