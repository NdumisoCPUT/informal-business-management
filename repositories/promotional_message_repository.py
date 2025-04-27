# repositories/promotional_message_repository.py

from repositories.repository import Repository
from src.promotional_message import PromotionalMessage

class PromotionalMessageRepository(Repository[PromotionalMessage, int]):
    pass
