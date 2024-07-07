from datetime import datetime

class FoodItem:
    def __init__(self, name, category, quantity, barcode, expiry_date):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.barcode = barcode
        self.expiry_date = expiry_date

    def __str__(self):
        return f"{self.name} ({self.category}), Quantity: {self.quantity}, Barcode: {self.barcode}, Expiry Date: {self.expiry_date}"
    
    def is_near_expiry(self, days_threshold=7):
        today = datetime.now().date()
        days_to_expiry = (self.expiry_date - today).days
        return days_to_expiry <= days_threshold
