from src.inventory_item import InventoryItem  # assuming structure for relationships

class Order:
    def __init__(self, order_id, status, date_created, total_amount):
        self.__order_id = order_id
        self.__status = status
        self.__date_created = date_created
        self.__total_amount = total_amount
        self.items = []  

    def submit(self):
        self.__status = "Submitted"
        print(f"Order {self.__order_id} submitted.")

    def cancel(self):
        self.__status = "Canceled"
        print(f"Order {self.__order_id} canceled.")

    def calculate_total(self):
        self.__total_amount = sum(item._InventoryItem__price for item in self.items)
        return self.__total_amount

    def add_item(self, item):
        if isinstance(item, InventoryItem):
            self.items.append(item)
        else:
            raise TypeError("Only InventoryItem objects can be added.")
