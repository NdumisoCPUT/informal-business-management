from repositories.payment_repository import PaymentRepository
from src.payment import Payment

class DatabasePaymentRepository(PaymentRepository):
    def save(self, entity: Payment) -> None:
        pass

    def find_by_id(self, id: int) -> Payment:
        pass

    def find_all(self) -> list[Payment]:
        pass

    def delete(self, id: int) -> None:
        pass
