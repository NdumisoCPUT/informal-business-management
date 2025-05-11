class InventoryItem:
    def __init__(self, item_id, name, quantity, price, restock_threshold):
        self.__item_id = item_id
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__restock_threshold = restock_threshold
        self.__status = self.__calculate_status()

    def __calculate_status(self):
        return "Low" if self.__quantity < self.__restock_threshold else "Available"

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

    def get_restock_threshold(self):
        return self.__restock_threshold

    def set_quantity(self, quantity):
        self.__quantity = quantity
        self.__status = self.__calculate_status()

    def set_status(self, status):
        self.__status = status

    def update_details(self, name=None, price=None, restock_threshold=None):
        if name is not None:
            self.__name = name
        if price is not None:
            self.__price = price
        if restock_threshold is not None:
            self.__restock_threshold = restock_threshold
        self.__status = self.__calculate_status()

    def __repr__(self):
        return (f"InventoryItem({self.__item_id}, {self.__name}, Qty: {self.__quantity}, "
                f"Price: {self.__price}, Status: {self.__status}, Threshold: {self.__restock_threshold})")
