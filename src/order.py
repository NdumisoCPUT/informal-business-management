class Order:
    def __init__(self, order_id, status, date, total_amount=0.0):
        self.order_id = order_id
        self.status = status
        self.date = date
        self.total_amount = total_amount
        self.items = []

    def get_order_id(self):
        return self.order_id

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        self.total_amount = sum(item.get_price() * item.get_quantity() for item in self.items)
        return self.total_amount

    def get_items(self):
        return self.items

    def get_total_amount(self):
        return self.total_amount
