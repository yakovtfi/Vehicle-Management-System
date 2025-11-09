from classes.vehicle import Vehicle
from classes.engine import Engine

class Car(Vehicle):
    def __init__(self, license_plate: str, year: int, engine: Engine):
        super().__init__(license_plate, year)
        self.engine = engine

    def calculate_annual_tax(self):
        base_tax = 500
        age = 2025 - self.get_year()
        tax = base_tax + (self.engine.horsepower * 0.5) - (age * 10)
        return max(tax, 200)
