from src.promotional_message import PromotionalMessage
from repositories.inmemory.promotional_message_repository import InMemoryPromotionalMessageRepository

class PromotionalMessageService:
    def __init__(self, repository: InMemoryPromotionalMessageRepository):
        self.repository = repository

    def create_message(self, message: PromotionalMessage):
        self.repository.add(message)
        return message

    def send_message(self, message_id: str):
        message = self.repository.get(message_id)
        if not message:
            raise ValueError("Message not found.")
        message.send()
        return message

    def archive_message(self, message_id: str):
        message = self.repository.get(message_id)
        if not message:
            raise ValueError("Message not found.")
        message.archive()
        return message

    def get_message(self, message_id: str):
        return self.repository.get(message_id)

    def list_messages(self):
        return self.repository.list_all()
