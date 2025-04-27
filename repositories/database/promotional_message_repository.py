from repositories.promotional_message_repository import PromotionalMessageRepository
from src.promotional_message import PromotionalMessage

class DatabasePromotionalMessageRepository(PromotionalMessageRepository):
    def save(self, entity: PromotionalMessage) -> None:
        pass

    def find_by_id(self, id: int) -> PromotionalMessage:
        pass

    def find_all(self) -> list[PromotionalMessage]:
        pass

    def delete(self, id: int) -> None:
        pass
