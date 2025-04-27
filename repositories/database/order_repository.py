# repositories/database/order_repository.py

from repositories.order_repository import OrderRepository
from src.order import Order

class DatabaseOrderRepository(OrderRepository):
    def save(self, entity: Order) -> None:
        pass

    def find_by_id(self, id: int) -> Order:
        pass

    def find_all(self) -> list[Order]:
        pass

    def delete(self, id: int) -> None:
        pass
