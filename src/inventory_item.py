class InventoryItem:
    def __init__(self, item_id, name, quantity, price, status):
        self.__item_id = item_id
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__status = status

    def get_item_id(self):
        return self.__item_id

    def get_name(self):
        return self.__name

    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    def get_status(self):
        return self.__status

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_status(self, status):
        self.__status = status

    def update_details(self, name=None, price=None):
        if name is not None:
            self.__name = name
        if price is not None:
            self.__price = price

    def __repr__(self):
        return f"InventoryItem({self.__item_id}, {self.__name}, Qty: {self.__quantity}, Price: {self.__price}, Status: {self.__status})"
