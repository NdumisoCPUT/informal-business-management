# src/system_settings.py

class SystemSettings:
    def __init__(self, setting_id, name, value, last_modified):
        self.__setting_id = setting_id
        self.__name = name
        self.__value = value
        self.__last_modified = last_modified

    def update_setting(self, new_value, modified_date):
        self.__value = new_value
        self.__last_modified = modified_date
        print(f"Setting '{self.__name}' updated to '{self.__value}' on {self.__last_modified}.")

    def restore_default(self):
        self.__value = "default"
        print(f"Setting '{self.__name}' has been restored to default.")

    def get_setting_id(self):
        return self.__setting_id

    def get_name(self):
        return self.__name

    def get_value(self):
        return self.__value

    def get_last_modified(self):
        return self.__last_modified

