class PromotionalMessage:
    def __init__(self, content, channel):
        self.content = content
        self.channel = channel

    def send(self):
        print(f"Sending '{self.content}' via {self.channel}")


class PromotionalMessageFactory:
    @staticmethod
    def create_message(message_type):
        if message_type == "email":
            return PromotionalMessage("Promo Email: 50% OFF!", "Email")
        elif message_type == "sms":
            return PromotionalMessage("SMS Deal: 2-for-1!", "SMS")
        elif message_type == "whatsapp":
            return PromotionalMessage("WhatsApp Alert: Free delivery!", "WhatsApp")
        else:
            raise ValueError("Unknown message type")
