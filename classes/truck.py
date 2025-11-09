from classes.vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, license_plate: str, year: int, max_load: float):
        super().__init__(license_plate, year)
        self.max_load = max_load

    def calculate_annual_tax(self):
        base_tax = 800
        tax = base_tax + (self.max_load * 0.2)
        return tax