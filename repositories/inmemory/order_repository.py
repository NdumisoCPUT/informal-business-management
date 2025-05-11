from src.order import Order

class InMemoryOrderRepository:
    def __init__(self):
        self._storage = {}

    def save(self, order: Order):
        self._storage[order.get_order_id()] = order
        return order

    def find_by_id(self, order_id: str):
        return self._storage.get(order_id)

    def list_all(self):
        return list(self._storage.values())

    def delete(self, order_id: str):
        return self._storage.pop(order_id, None)
