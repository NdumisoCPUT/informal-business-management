import unittest
from src.user_account import UserAccount
from repositories.inmemory.user_account_repository import InMemoryUserAccountRepository
from services.user_account_service import UserAccountService

class TestUserAccountService(unittest.TestCase):

    def setUp(self):
        self.repo = InMemoryUserAccountRepository()
        self.service = UserAccountService(self.repo)

    def test_create_and_find_user(self):
        user = UserAccount("U001", "Alice", "alice@example.com", "pass123", "admin")
        self.service.create_user(user)

        found_user = self.service.find_user("U001")
        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.get_user_id(), "U001")
        self.assertEqual(found_user.get_name(), "Alice")

    def test_update_profile(self):
        user = UserAccount("U002", "Bob", "bob@example.com", "pass456", "customer")
        self.service.create_user(user)

        # Simulate profile update
        user.update_profile(new_name="Bobby", new_email="bobby@example.com")
        self.service.update_profile(user)

        updated_user = self.service.find_user("U002")
        self.assertEqual(updated_user.get_name(), "Bobby")
        self.assertEqual(updated_user.get_email(), "bobby@example.com")

if __name__ == '__main__':
    unittest.main()
