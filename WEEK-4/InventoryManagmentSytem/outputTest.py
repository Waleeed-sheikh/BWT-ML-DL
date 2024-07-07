from datetime import datetime
from inventory_management.food_item import FoodItem
from inventory_management.inventory import Inventory

inventory = Inventory()

inventory.add_item(FoodItem("Apple", "Fruit", 10, "1234567890", datetime(2024, 7, 10).date()))
inventory.add_item(FoodItem("Milk", "Dairy", 5, "0987654321", datetime(2024, 7, 5).date()))

inventory.edit_item("1234567890", quantity=15)

inventory.delete_item("0987654321")

item = inventory.search_item("1234567890")
print(f"Found: {item}")

near_expiry_items = inventory.handle_near_expiry_items()
print("Near expiry items:")
for item in near_expiry_items:
    print(item)
