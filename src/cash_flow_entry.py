# src/cash_flow_entry.py

class CashFlowEntry:
    def __init__(self, entry_id, amount, entry_type, status, date):
        self.__entry_id = entry_id
        self.__amount = amount
        self.__type = entry_type  # "income" or "expense"
        self.__status = status    # "active" or "archived"
        self.__date = date

    def validate_entry(self):
        return self.__amount > 0 and self.__type in ["income", "expense"]

    def archive_entry(self):
        self.__status = "archived"
        print(f"Entry {self.__entry_id} archived successfully.")

    def get_entry_id(self):
        return self.__entry_id

    def get_amount(self):
        return self.__amount

    def get_type(self):
        return self.__type

    def get_status(self):
        return self.__status

    def get_date(self):
        return self.__date

