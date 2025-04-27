# repositories/filesystem/user_account_repository.py

import os
import json
from src.user_account import UserAccount

class FileSystemUserAccountRepository:
    def __init__(self, storage_dir="data/user_accounts"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def _get_user_filepath(self, user_id):
        return os.path.join(self.storage_dir, f"user_{user_id}.json")

    def add(self, user):
        if not isinstance(user, UserAccount):
            raise TypeError("Only UserAccount objects can be added.")

        filepath = self._get_user_filepath(user.get_user_id())
        with open(filepath, 'w') as f:
            json.dump({
                "user_id": user.get_user_id(),
                "name": user.get_name(),
                "email": user.get_email(),
                "role": user.get_role()
            }, f, indent=4)

    def get(self, user_id):
        filepath = self._get_user_filepath(user_id)
        if not os.path.exists(filepath):
            return None

        with open(filepath, 'r') as f:
            data = json.load(f)
            user = UserAccount(
                user_id=data["user_id"],
                name=data["name"],
                email=data["email"],
                password="hidden",  # Password should NOT be read back in real systems
                role=data["role"]
            )
            return user

    def remove(self, user_id):
        filepath = self._get_user_filepath(user_id)
        if os.path.exists(filepath):
            os.remove(filepath)

    def list_all(self):
        users = []
        for filename in os.listdir(self.storage_dir):
            if filename.startswith("user_") and filename.endswith(".json"):
                user_id = int(filename.replace("user_", "").replace(".json", ""))
                user = self.get(user_id)
                if user:
                    users.append(user)
        return users
