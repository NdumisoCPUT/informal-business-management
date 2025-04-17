from src.user_account import UserAccount
from src.inventory_item import InventoryItem
from src.order import Order

# Create a user
user = UserAccount("U001", "Ndumiso", "ndumiso@example.com", "password123", "admin")
user.login()
user.update_profile(new_name="Mr. Ngcobo")

# Create inventory items
item1 = InventoryItem("I001", "Milk", 10, 25.50, 5)
item2 = InventoryItem("I002", "Bread", 5, 15.75, 2)

# Create an order and add items
order = Order("O1001", "New", "2025-04-17", 0)
order.add_item(item1)
order.add_item(item2)
total = order.calculate_total()

print(f"Order Total: R{total}")
order.submit()
