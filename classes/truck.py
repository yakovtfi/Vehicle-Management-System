from classes.vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, license_plate: str, year: int):
        super().__init__(license_plate, year)

    def calculate_annual_tax(self):
        base_tax = 1000
        age = 2025 - self.get_year()
        tax = base_tax + (self.engine.horsepower * 0.5) - (age * 10)
        return max(tax, 200)
