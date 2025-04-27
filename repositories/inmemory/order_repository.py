
from src.order import Order

class InMemoryOrderRepository:
    def __init__(self):
        self.orders = {}

    def add(self, order):
        if isinstance(order, Order):
            self.orders[order._Order__order_id] = order
        else:
            raise TypeError("Only Order objects can be added.")

    def get(self, order_id):
        return self.orders.get(order_id)

    def remove(self, order_id):
        if order_id in self.orders:
            del self.orders[order_id]

    def list_all(self):
        return list(self.orders.values())
