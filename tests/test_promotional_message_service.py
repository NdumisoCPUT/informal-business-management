import unittest
from datetime import datetime
from src.promotional_message import PromotionalMessage
from repositories.inmemory.promotional_message_repository import InMemoryPromotionalMessageRepository
from services.promotional_message_service import PromotionalMessageService

class TestPromotionalMessageService(unittest.TestCase):

    def setUp(self):
        self.repo = InMemoryPromotionalMessageRepository()
        self.service = PromotionalMessageService(self.repo)

    def test_create_and_get_message(self):
        msg = PromotionalMessage("MSG001", "Sale starts today!", "active", datetime.now())
        self.service.create_message(msg)

        result = self.service.get_message("MSG001")
        self.assertEqual(result.get_message_id(), "MSG001")
        self.assertEqual(result.get_status(), "active")

    def test_send_message(self):
        msg = PromotionalMessage("MSG002", "New products in stock!", "draft", datetime.now())
        self.repo.add(msg)

        sent = self.service.send_message("MSG002")
        self.assertEqual(sent.get_status(), "sent")

    def test_archive_message(self):
        msg = PromotionalMessage("MSG003", "Limited offer ends soon!", "sent", datetime.now())
        self.repo.add(msg)

        archived = self.service.archive_message("MSG003")
        self.assertEqual(archived.get_status(), "archived")

    def test_list_messages(self):
        msg1 = PromotionalMessage("MSG004", "Hello", "active", datetime.now())
        msg2 = PromotionalMessage("MSG005", "Goodbye", "archived", datetime.now())
        self.repo.add(msg1)
        self.repo.add(msg2)

        all_msgs = self.service.list_messages()
        self.assertEqual(len(all_msgs), 2)

if __name__ == '__main__':
    unittest.main()
