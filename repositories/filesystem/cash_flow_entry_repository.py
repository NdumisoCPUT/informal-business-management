# repositories/filesystem/cash_flow_entry_repository.py

import os
import json
from src.cash_flow_entry import CashFlowEntry

class FileSystemCashFlowEntryRepository:
    def __init__(self, storage_dir="data/cash_flow_entries"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def _get_entry_filepath(self, entry_id):
        return os.path.join(self.storage_dir, f"cash_flow_entry_{entry_id}.json")

    def add(self, entry):
        if not isinstance(entry, CashFlowEntry):
            raise TypeError("Only CashFlowEntry objects can be added.")

        filepath = self._get_entry_filepath(entry.get_entry_id())
        with open(filepath, 'w') as f:
            json.dump({
                "entry_id": entry.get_entry_id(),
                "amount": entry.get_amount(),
                "type": entry.get_type(),
                "status": entry.get_status(),
                "date": entry.get_date()
            }, f, indent=4)

    def get(self, entry_id):
        filepath = self._get_entry_filepath(entry_id)
        if not os.path.exists(filepath):
            return None

        with open(filepath, 'r') as f:
            data = json.load(f)
            entry = CashFlowEntry(
                entry_id=data["entry_id"],
                amount=data["amount"],
                entry_type=data["type"],
                status=data["status"],
                date=data["date"]
            )
            return entry

    def remove(self, entry_id):
        filepath = self._get_entry_filepath(entry_id)
        if os.path.exists(filepath):
            os.remove(filepath)

    def list_all(self):
        entries = []
        for filename in os.listdir(self.storage_dir):
            if filename.startswith("cash_flow_entry_") and filename.endswith(".json"):
                entry_id = int(filename.replace("cash_flow_entry_", "").replace(".json", ""))
                entry = self.get(entry_id)
                if entry:
                    entries.append(entry)
        return entries
