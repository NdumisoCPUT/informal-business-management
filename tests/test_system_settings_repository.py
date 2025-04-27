# tests/test_system_settings_repository.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
from repositories.inmemory.system_settings_repository import InMemorySystemSettingsRepository
from src.system_settings import SystemSettings

class TestInMemorySystemSettingsRepository(unittest.TestCase):

    def setUp(self):
        self.repo = InMemorySystemSettingsRepository()
        self.setting = SystemSettings(
            setting_id=1,
            name="Theme",
            value="Dark Mode",
            last_modified="2024-04-27"
        )

    def test_add_and_get_setting(self):
        self.repo.add(self.setting)
        retrieved = self.repo.get(1)
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.get_value(), "Dark Mode")

    def test_remove_setting(self):
        self.repo.add(self.setting)
        self.repo.remove(1)
        self.assertIsNone(self.repo.get(1))

    def test_list_all_settings(self):
        self.repo.add(self.setting)
        settings = self.repo.list_all()
        self.assertEqual(len(settings), 1)
        self.assertEqual(settings[0].get_setting_id(), 1)

if __name__ == "__main__":
    unittest.main()
