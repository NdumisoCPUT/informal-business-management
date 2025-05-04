import unittest
from datetime import datetime
from src.system_settings import SystemSettings
from repositories.inmemory.system_settings_repository import InMemorySystemSettingsRepository
from services.system_settings_service import SystemSettingsService

class TestSystemSettingsService(unittest.TestCase):

    def setUp(self):
        self.repo = InMemorySystemSettingsRepository()
        self.service = SystemSettingsService(self.repo)

    def test_add_and_get_setting(self):
        setting = SystemSettings("SET001", "theme", "dark", datetime.now())
        self.service.add_setting(setting)

        result = self.service.get_setting("SET001")
        self.assertIsNotNone(result)
        self.assertEqual(result.get_value(), "dark")

    def test_update_setting(self):
        setting = SystemSettings("SET002", "notifications", "on", datetime.now())
        self.repo.add(setting)

        self.service.update_setting("SET002", "off", datetime.now())
        updated = self.service.get_setting("SET002")

        self.assertEqual(updated.get_value(), "off")

    def test_restore_default(self):
        setting = SystemSettings("SET003", "language", "French", datetime.now())
        self.repo.add(setting)

        self.service.restore_setting("SET003")
        restored = self.service.get_setting("SET003")

        self.assertEqual(restored.get_value(), "default")

    def test_list_settings(self):
        setting1 = SystemSettings("SET004", "volume", "medium", datetime.now())
        setting2 = SystemSettings("SET005", "timezone", "UTC+2", datetime.now())
        self.repo.add(setting1)
        self.repo.add(setting2)

        settings = self.service.list_settings()
        self.assertEqual(len(settings), 2)

if __name__ == '__main__':
    unittest.main()
