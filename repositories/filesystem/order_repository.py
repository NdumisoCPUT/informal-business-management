# repositories/filesystem/order_repository.py

import os
import json
from src.order import Order
from src.inventory_item import InventoryItem

class FileSystemOrderRepository:
    def __init__(self, storage_dir="data/orders"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def _get_order_filepath(self, order_id):
        return os.path.join(self.storage_dir, f"order_{order_id}.json")

    def add(self, order):
        if not isinstance(order, Order):
            raise TypeError("Only Order objects can be added.")

        filepath = self._get_order_filepath(order._Order__order_id)
        with open(filepath, 'w') as f:
            json.dump({
                "order_id": order._Order__order_id,
                "status": order._Order__status,
                "date_created": order._Order__date_created,
                "total_amount": order._Order__total_amount,
                "items": [
                    {
                        "item_id": item._InventoryItem__item_id,
                        "name": item._InventoryItem__name,
                        "price": item._InventoryItem__price
                    }
                    for item in order.items
                ]
            }, f, indent=4)

    def get(self, order_id):
        filepath = self._get_order_filepath(order_id)
        if not os.path.exists(filepath):
            return None

        with open(filepath, 'r') as f:
            data = json.load(f)
            order = Order(
                order_id=data["order_id"],
                status=data["status"],
                date_created=data["date_created"],
                total_amount=data["total_amount"]
            )
            for item_data in data["items"]:
                item = InventoryItem(
                    item_id=item_data["item_id"],
                    name=item_data["name"],
                    price=item_data["price"]
                )
                order.add_item(item)
            return order

    def remove(self, order_id):
        filepath = self._get_order_filepath(order_id)
        if os.path.exists(filepath):
            os.remove(filepath)

    def list_all(self):
        orders = []
        for filename in os.listdir(self.storage_dir):
            if filename.startswith("order_") and filename.endswith(".json"):
                order_id = int(filename.replace("order_", "").replace(".json", ""))
                order = self.get(order_id)
                if order:
                    orders.append(order)
        return orders
