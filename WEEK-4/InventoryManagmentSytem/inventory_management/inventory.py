import csv
from datetime import datetime
from inventory_management.food_item import FoodItem

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added: {item}")

    def edit_item(self, barcode, name=None, category=None, quantity=None, expiry_date=None):
        for item in self.items:
            if item.barcode == barcode:
                if name:
                    item.name = name
                if category:
                    item.category = category
                if quantity:
                    item.quantity = quantity
                if expiry_date:
                    item.expiry_date = expiry_date
                print(f"Edited: {item}")
                return
        print(f"Item with barcode {barcode} not found.")

    def delete_item(self, barcode):
        for item in self.items:
            if item.barcode == barcode:
                self.items.remove(item)
                print(f"Deleted: {item}")
                return
        print(f"Item with barcode {barcode} not found.")

    def search_item(self, barcode):
        for item in self.items:
            if item.barcode == barcode:
                return item
        return None

    def handle_near_expiry_items(self, days_threshold=7):
        near_expiry_items = [item for item in self.items if item.is_near_expiry(days_threshold)]
        return near_expiry_items

    def save_to_csv(self, filename):
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Category', 'Quantity', 'Barcode', 'Expiry Date'])
                for item in self.items:
                    writer.writerow([item.name, item.category, item.quantity, item.barcode, item.expiry_date])
            print(f"Inventory saved to {filename}")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_csv(self, filename):
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                self.items = []
                for row in reader:
                    item = FoodItem(row['Name'], row['Category'], int(row['Quantity']), row['Barcode'], datetime.strptime(row['Expiry Date'], '%Y-%m-%d').date())
                    self.items.append(item)
            print(f"Inventory loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error loading from file: {e}")
