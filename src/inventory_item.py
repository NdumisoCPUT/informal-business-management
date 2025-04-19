class InventoryItem:
    def __init__(self, item_id, name, quantity, price, restock_threshold):
        self.__item_id = item_id
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__restock_threshold = restock_threshold

    def update_stock(self, quantity):
       
        self.__quantity += quantity

    def check_availability(self):
       
        return self.__quantity > 0
