class UserAccount:
    def __init__(self, user_id, name, email, password, role):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__password = password
        self.__role = role

    def login(self):
       
        print(f"User {self.__email} attempting login...")

    def logout(self):
        
        print(f"User {self.__email} logged out.")

    def update_profile(self, new_name=None, new_email=None):
       
        if new_name:
            self.__name = new_name
        if new_email:
            self.__email = new_email
        print("Profile updated.")
