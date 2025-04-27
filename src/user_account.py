# src/user_account.py

class UserAccount:
    def __init__(self, user_id, name, email, password, role):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__password = password  # In a real system, you would encrypt this!
        self.__role = role  # Example: "Admin", "Staff", "Customer"

    def login(self):
        print(f"User {self.__email} attempting login...")

    def logout(self):
        print(f"User {self.__email} has successfully logged out.")

    def update_profile(self, new_name=None, new_email=None):
        if new_name:
            self.__name = new_name
        if new_email:
            self.__email = new_email
        print(f"Profile for user {self.__user_id} updated.")

    # Getter methods
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_role(self):
        return self.__role

