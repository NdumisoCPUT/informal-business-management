# repositories/user_account_repository.py

from repositories.repository import Repository
from src.user_account import UserAccount

class UserAccountRepository(Repository[UserAccount, int]):
    pass
