from abc import ABC, abstractmethod

class InventoryItem(ABC):
    @abstractmethod
    def create(self):
        pass

class Bread(InventoryItem):
    def create(self):
        print("Creating Bread Item")

class Juice(InventoryItem):
    def create(self):
        print("Creating Juice Item")

class ItemFactory(ABC):
    @abstractmethod
    def create_item(self):
        pass

class BakeryFactory(ItemFactory):
    def create_item(self):
        return Bread()

class BeverageFactory(ItemFactory):
    def create_item(self):
        return Juice()
