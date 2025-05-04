# repositories/inmemory/order_repository.py

class InMemoryOrderRepository:
    def __init__(self):
        self.orders = {}

    def save(self, order):
        self.orders[order.get_order_id()] = order

    def find_by_id(self, order_id):
        return self.orders.get(order_id)

    def delete(self, order_id):
        if order_id in self.orders:
            del self.orders[order_id]

    def list_all(self):
        return list(self.orders.values())
