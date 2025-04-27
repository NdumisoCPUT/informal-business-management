# src/payment.py

class Payment:
    def __init__(self, payment_id, amount, method, status, timestamp):
        self.__payment_id = payment_id
        self.__amount = amount
        self.__method = method
        self.__status = status
        self.__timestamp = timestamp

    def process(self):
        if self.validate():
            self.__status = "Completed"
            print(f"Payment {self.__payment_id} processed successfully.")
        else:
            self.__status = "Failed"
            print(f"Payment {self.__payment_id} failed to process.")

    def retry(self):
        if self.__status == "Failed":
            print(f"Retrying payment {self.__payment_id}...")
            self.process()
        else:
            print(f"Payment {self.__payment_id} does not need retrying (status: {self.__status}).")

    def validate(self):
        if self.__amount > 0 and self.__method in ["Card", "Cash", "EFT", "MobileMoney"]:
            return True
        return False

    def get_payment_id(self):
        return self.__payment_id

    def get_amount(self):
        return self.__amount

    def get_status(self):
        return self.__status

    def get_method(self):
        return self.__method

    def get_timestamp(self):
        return self.__timestamp
