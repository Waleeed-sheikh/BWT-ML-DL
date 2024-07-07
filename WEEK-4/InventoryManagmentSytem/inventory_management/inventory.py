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

    def search_item(self, barcode=None, name=None, category=None):
        results = []
        for item in self.items:
            if barcode and item.barcode == barcode:
                results.append(item)
            elif name and item.name == name:
                results.append(item)
            elif category and item.category == category:
                results.append(item)
        return results

    def generate_report(self, report_type):
        if report_type == 'near_expiry':
            return self.handle_near_expiry_items()
        elif report_type == 'low_stock':
            return [item for item in self.items if item.quantity < 5]
        elif report_type == 'category_summary':
            summary = {}
            for item in self.items:
                if item.category not in summary:
                    summary[item.category] = 0
                summary[item.category] += item.quantity
            return summary

    def handle_near_expiry_items(self, days_threshold=7):
        near_expiry_items = [item for item in self.items if item.is_near_expiry(days_threshold)]
        return near_expiry_items
