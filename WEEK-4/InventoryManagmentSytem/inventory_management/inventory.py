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

    def __iter__(self):
        return iter(self.items)

    def near_expiry_items_generator(self, days_threshold=7):
        for item in self.items:
            if item.is_near_expiry(days_threshold):
                yield item
