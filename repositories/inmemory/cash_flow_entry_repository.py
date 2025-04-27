# repositories/inmemory/cash_flow_entry_repository.py

from src.cash_flow_entry import CashFlowEntry

class InMemoryCashFlowEntryRepository:
    def __init__(self):
        self.entries = {}

    def add(self, entry):
        if isinstance(entry, CashFlowEntry):
            self.entries[entry.get_entry_id()] = entry
        else:
            raise TypeError("Only CashFlowEntry objects can be added.")

    def get(self, entry_id):
        return self.entries.get(entry_id)

    def remove(self, entry_id):
        if entry_id in self.entries:
            del self.entries[entry_id]

    def list_all(self):
        return list(self.entries.values())
