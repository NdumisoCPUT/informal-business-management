from datetime import datetime

class Payment:
    def __init__(self, payment_id: str, amount: float, method: str, status: str, date: datetime):
        self.__payment_id = payment_id
        self.__amount = amount
        self.__method = method
        self.__status = status
        self.__date = date

    def process(self):
        if self.__amount > 0:
            self.__status = "Completed"
        else:
            self.__status = "Failed"

    def retry(self):
        self.process()  # Retry means re-processing under updated conditions

    def get_payment_id(self):
        return self.__payment_id

    def get_status(self):
        return self.__status

    def get_amount(self):
        return self.__amount

    def get_method(self):
        return self.__method

    def get_date(self):
        return self.__date

