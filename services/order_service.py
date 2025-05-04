# services/order_service.py

from src.order import Order
from repositories.inmemory.order_repository import InMemoryOrderRepository

class OrderService:
    def __init__(self, repository: InMemoryOrderRepository):
        self.repository = repository

    def create_order(self, order: Order):
        order.calculate_total()
        self.repository.save(order)
        return order

    def get_order(self, order_id: str):
        return self.repository.find_by_id(order_id)

    def list_orders(self):
        return self.repository.list_all()

    def delete_order(self, order_id: str):
        self.repository.delete(order_id)
