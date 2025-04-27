# tests/test_user_account_repository.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
from repositories.inmemory.user_account_repository import InMemoryUserAccountRepository
from src.user_account import UserAccount

class TestInMemoryUserAccountRepository(unittest.TestCase):

    def setUp(self):
        self.repo = InMemoryUserAccountRepository()
        self.user = UserAccount(
            user_id=1,
            name="John Doe",
            email="john@example.com",
            password="1234",
            role="Admin"
        )

    def test_add_and_get_user(self):
        self.repo.add(self.user)
        retrieved = self.repo.get(1)
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.get_email(), "john@example.com")

    def test_remove_user(self):
        self.repo.add(self.user)
        self.repo.remove(1)
        self.assertIsNone(self.repo.get(1))

    def test_list_all_users(self):
        self.repo.add(self.user)
        users = self.repo.list_all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].get_user_id(), 1)

if __name__ == "__main__":
    unittest.main()
