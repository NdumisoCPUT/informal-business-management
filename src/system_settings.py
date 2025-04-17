class SystemSettings:
    def __init__(self, setting_id, name, value, last_modified):
        self.__setting_id = setting_id
        self.__name = name
        self.__value = value
        self.__last_modified = last_modified

    def update_setting(self, new_value, modified_date):
        # Update the value and timestamp
        self.__value = new_value
        self.__last_modified = modified_date

    def restore_default(self):
        # Restores value to some default (hardcoded for now)
        self.__value = "default"
