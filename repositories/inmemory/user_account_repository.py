from src.user_account import UserAccount

class InMemoryUserAccountRepository:
    def __init__(self):
        self.users = {}

    def add(self, user):
        if isinstance(user, UserAccount):
            self.users[user.get_user_id()] = user
        else:
            raise TypeError("Only UserAccount objects can be added.")

    def save(self, user):
        self.add(user)

    def get(self, user_id):
        return self.users.get(user_id)

    def find_by_id(self, user_id):
        return self.get(user_id)

    def remove(self, user_id):
        if user_id in self.users:
            del self.users[user_id]

    def list_all(self):
        return list(self.users.values())

