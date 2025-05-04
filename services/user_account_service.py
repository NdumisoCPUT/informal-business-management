
# user_account_service.py
from repositories.inmemory.user_account_repository import InMemoryUserAccountRepository
from src.user_account import UserAccount

class UserAccountService:
    def __init__(self, repository: InMemoryUserAccountRepository):
        self.repository = repository

    def create_user(self, user: UserAccount):
        self.repository.save(user)

    def find_user(self, user_id: str):
        return self.repository.find_by_id(user_id)

    def update_profile(self, user: UserAccount):
        self.repository.save(user)