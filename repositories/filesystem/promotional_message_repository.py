# repositories/filesystem/promotional_message_repository.py

import os
import json
from src.promotional_message import PromotionalMessage

class FileSystemPromotionalMessageRepository:
    def __init__(self, storage_dir="data/promotional_messages"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def _get_message_filepath(self, message_id):
        return os.path.join(self.storage_dir, f"promotional_message_{message_id}.json")

    def add(self, message):
        if not isinstance(message, PromotionalMessage):
            raise TypeError("Only PromotionalMessage objects can be added.")

        filepath = self._get_message_filepath(message.get_message_id())
        with open(filepath, 'w') as f:
            json.dump({
                "message_id": message.get_message_id(),
                "content": message._PromotionalMessage__content,
                "channel": message._PromotionalMessage__channel,
                "target_group": message._PromotionalMessage__target_group,
                "sent_date": message._PromotionalMessage__sent_date
            }, f, indent=4)

    def get(self, message_id):
        filepath = self._get_message_filepath(message_id)
        if not os.path.exists(filepath):
            return None

        with open(filepath, 'r') as f:
            data = json.load(f)
            message = PromotionalMessage(
                message_id=data["message_id"],
                content=data["content"],
                channel=data["channel"],
                target_group=data["target_group"],
                sent_date=data["sent_date"]
            )
            return message

    def remove(self, message_id):
        filepath = self._get_message_filepath(message_id)
        if os.path.exists(filepath):
            os.remove(filepath)

    def list_all(self):
        messages = []
        for filename in os.listdir(self.storage_dir):
            if filename.startswith("promotional_message_") and filename.endswith(".json"):
                message_id = int(filename.replace("promotional_message_", "").replace(".json", ""))
                message = self.get(message_id)
                if message:
                    messages.append(message)
        return messages
