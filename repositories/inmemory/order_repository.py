from src.order import Order

class InMemoryOrderRepository:
    def __init__(self):
        self._storage = {}

    def add_order(self, order: Order):
        self._storage[order.get_order_id()] = order
        return order

    def get_order(self, order_id: str):
        return self._storage.get(order_id)

    def list_orders(self):
        return list(self._storage.values())

    def remove_order(self, order_id: str):
        return self._storage.pop(order_id, None)
