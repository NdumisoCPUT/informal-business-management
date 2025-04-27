# repositories/inmemory/promotional_message_repository.py

from src.promotional_message import PromotionalMessage

class InMemoryPromotionalMessageRepository:
    def __init__(self):
        self.messages = {}

    def add(self, message):
        if isinstance(message, PromotionalMessage):
            self.messages[message.get_message_id()] = message
        else:
            raise TypeError("Only PromotionalMessage objects can be added.")

    def get(self, message_id):
        return self.messages.get(message_id)

    def remove(self, message_id):
        if message_id in self.messages:
            del self.messages[message_id]

    def list_all(self):
        return list(self.messages.values())
