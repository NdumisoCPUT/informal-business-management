from src.system_settings import SystemSettings
from repositories.inmemory.system_settings_repository import InMemorySystemSettingsRepository

class SystemSettingsService:
    def __init__(self, repository: InMemorySystemSettingsRepository):
        self.repository = repository

    def add_setting(self, setting: SystemSettings):
        self.repository.add(setting)
        return setting

    def update_setting(self, setting_id, new_value, modified_date):
        setting = self.repository.get(setting_id)
        if not setting:
            raise ValueError("Setting not found.")
        setting.update_setting(new_value, modified_date)
        return setting

    def restore_setting(self, setting_id):
        setting = self.repository.get(setting_id)
        if not setting:
            raise ValueError("Setting not found.")
        setting.restore_default()
        return setting

    def get_setting(self, setting_id):
        return self.repository.get(setting_id)

    def list_settings(self):
        return self.repository.list_all()
