class CashFlowEntry:
    def __init__(self, entry_id, amount, entry_type, status, date):
        self.__entry_id = entry_id
        self.__amount = amount
        self.__type = entry_type  
        self.__status = status    
        self.__date = date

    def validate_entry(self):
        
        return self.__amount > 0 and self.__type in ["income", "expense"]

    def archive_entry(self):
        
        self.__status = "archived"
