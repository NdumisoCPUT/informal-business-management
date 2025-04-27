# repositories/filesystem/system_settings_repository.py

import os
import json
from src.system_settings import SystemSettings

class FileSystemSystemSettingsRepository:
    def __init__(self, storage_dir="data/system_settings"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def _get_setting_filepath(self, setting_id):
        return os.path.join(self.storage_dir, f"setting_{setting_id}.json")

    def add(self, setting):
        if not isinstance(setting, SystemSettings):
            raise TypeError("Only SystemSettings objects can be added.")

        filepath = self._get_setting_filepath(setting.get_setting_id())
        with open(filepath, 'w') as f:
            json.dump({
                "setting_id": setting.get_setting_id(),
                "name": setting.get_name(),
                "value": setting.get_value(),
                "last_modified": setting.get_last_modified()
            }, f, indent=4)

    def get(self, setting_id):
        filepath = self._get_setting_filepath(setting_id)
        if not os.path.exists(filepath):
            return None

        with open(filepath, 'r') as f:
            data = json.load(f)
            setting = SystemSettings(
                setting_id=data["setting_id"],
                name=data["name"],
                value=data["value"],
                last_modified=data["last_modified"]
            )
            return setting

    def remove(self, setting_id):
        filepath = self._get_setting_filepath(setting_id)
        if os.path.exists(filepath):
            os.remove(filepath)

    def list_all(self):
        settings = []
        for filename in os.listdir(self.storage_dir):
            if filename.startswith("setting_") and filename.endswith(".json"):
                setting_id = int(filename.replace("setting_", "").replace(".json", ""))
                setting = self.get(setting_id)
                if setting:
                    settings.append(setting)
        return settings
