from repositories.system_settings_repository import SystemSettingsRepository
from src.system_settings import SystemSettings

class DatabaseSystemSettingsRepository(SystemSettingsRepository):
    def save(self, entity: SystemSettings) -> None:
        pass

    def find_by_id(self, id: int) -> SystemSettings:
        pass

    def find_all(self) -> list[SystemSettings]:
        pass

    def delete(self, id: int) -> None:
        pass
