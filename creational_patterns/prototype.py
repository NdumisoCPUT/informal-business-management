import copy

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

    def display(self):
        print(f"Order ID: {self.order_id}, Items: {self.items}")

    def clone(self):
        return copy.deepcopy(self)

class OrderPrototypeRegistry:
    def __init__(self):
        self._orders = {}

    def register(self, key, order):
        self._orders[key] = order

    def clone(self, key):
        return self._orders[key].clone()
