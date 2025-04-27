from repositories.cash_flow_entry_repository import CashFlowEntryRepository
from src.cash_flow_entry import CashFlowEntry

class DatabaseCashFlowEntryRepository(CashFlowEntryRepository):
    def save(self, entity: CashFlowEntry) -> None:
        pass

    def find_by_id(self, id: int) -> CashFlowEntry:
        pass

    def find_all(self) -> list[CashFlowEntry]:
        pass

    def delete(self, id: int) -> None:
        pass
