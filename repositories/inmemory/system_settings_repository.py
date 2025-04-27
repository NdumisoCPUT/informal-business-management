# repositories/inmemory/system_settings_repository.py

from src.system_settings import SystemSettings

class InMemorySystemSettingsRepository:
    def __init__(self):
        self.settings = {}

    def add(self, setting):
        if isinstance(setting, SystemSettings):
            self.settings[setting.get_setting_id()] = setting
        else:
            raise TypeError("Only SystemSettings objects can be added.")

    def get(self, setting_id):
        return self.settings.get(setting_id)

    def remove(self, setting_id):
        if setting_id in self.settings:
            del self.settings[setting_id]

    def list_all(self):
        return list(self.settings.values())
