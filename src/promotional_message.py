from datetime import datetime

class PromotionalMessage:
    def __init__(self, message_id, content, channel, target_group, sent_date: datetime):
        self.__message_id = message_id
        self.__content = content
        self.__channel = channel
        self.__target_group = target_group
        self.__sent_date = sent_date
        self.__archived = False  

    def create_message(self):
        return f"Message to {self.__target_group} via {self.__channel}: {self.__content}"

    def send(self):
        print(f"Sending: {self.create_message()}")

    def log_delivery(self):
        print(f"Message {self.__message_id} delivered on {self.__sent_date}")

    def archive(self):
        self.__archived = True

    def is_archived(self):
        return self.__archived

    def get_message_id(self):
        return self.__message_id

    def get_sent_date(self):
        return self.__sent_date

