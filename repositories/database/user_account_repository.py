from repositories.user_account_repository import UserAccountRepository
from src.user_account import UserAccount

class DatabaseUserAccountRepository(UserAccountRepository):
    def save(self, entity: UserAccount) -> None:
        pass

    def find_by_id(self, id: int) -> UserAccount:
        pass

    def find_all(self) -> list[UserAccount]:
        pass

    def delete(self, id: int) -> None:
        pass
