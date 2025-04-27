
from repositories.repository import Repository
from src.order import Order

class OrderRepository(Repository[Order, int]):
    pass
