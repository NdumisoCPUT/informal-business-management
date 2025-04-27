import json
import os
from typing import Optional, List
from repositories.inventory_item_repository import InventoryItemRepository
from src.inventory_item import InventoryItem

class FileSystemInventoryItemRepository(InventoryItemRepository):
    def __init__(self, file_path: str = "inventory_items.json"):
        self._file_path = file_path

    def save(self, item: InventoryItem) -> None:
        items = self._load_all_as_dict()
        items[item.id] = {
            "id": item.id,
            "name": item.name,
            "quantity": item.quantity,
            "price": item.price,
            "restock_threshold": item.restock_threshold
        }
        self._write_all_as_dict(items)

    def find_by_id(self, id: str) -> Optional[InventoryItem]:
        items = self._load_all_as_dict()
        item_data = items.get(id)
        if item_data:
            return InventoryItem(**item_data)
        return None

    def find_all(self) -> List[InventoryItem]:
        items = self._load_all_as_dict()
        return [InventoryItem(**data) for data in items.values()]

    def delete(self, id: str) -> None:
        items = self._load_all_as_dict()
        items.pop(id, None)
        self._write_all_as_dict(items)

    def _load_all_as_dict(self) -> dict:
        if not os.path.exists(self._file_path):
            return {}
        with open(self._file_path, 'r') as f:
            return json.load(f)

    def _write_all_as_dict(self, items: dict) -> None:
        with open(self._file_path, 'w') as f:
            json.dump(items, f)
