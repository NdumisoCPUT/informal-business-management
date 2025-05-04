class CashFlowService:
    def __init__(self, repository):
        self.repository = repository

    def add_entry(self, entry):
        if not entry.validate_entry():
            raise ValueError("Invalid cash flow entry.")
        self.repository.add(entry)
        return entry

    def archive_entry(self, entry_id):
        entry = self.repository.get(entry_id)
        if not entry:
            return None
        entry.archive_entry()
        return entry

    def get_entry(self, entry_id):
        return self.repository.get(entry_id)

    def list_entries(self):
        return self.repository.list_all()

    def update_entry(self, entry_id, updated_entry):
        entry = self.repository.get(entry_id)
        if not entry:
            return None
        self.repository.add(updated_entry)
        return updated_entry
