import csv
from datetime import datetime
from inventory_management.food_item import FoodItem

def save_to_csv(inventory, filename):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Category', 'Quantity', 'Barcode', 'Expiry Date'])
            for item in inventory.items:
                writer.writerow([item.name, item.category, item.quantity, item.barcode, item.expiry_date])
        print(f"Inventory saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

def load_from_csv(inventory, filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            inventory.items = []
            for row in reader:
                item = FoodItem(row['Name'], row['Category'], int(row['Quantity']), row['Barcode'], datetime.strptime(row['Expiry Date'], '%Y-%m-%d').date())
                inventory.items.append(item)
        print(f"Inventory loaded from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"Error loading from file: {e}")
