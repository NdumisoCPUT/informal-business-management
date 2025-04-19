class Payment:
    def __init__(self, payment_id, amount, method, status, timestamp):
        self.__payment_id = payment_id
        self.__amount = amount
        self.__method = method
        self.__status = status
        self.__timestamp = timestamp

    def process(self):
     
        pass

    def retry(self):
       
        pass

    def validate(self):
       
        pass
