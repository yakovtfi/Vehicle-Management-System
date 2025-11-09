from classes.car import Car
from classes.electricMixin import ElectricMixin
from classes.engine import Engine
from classes.luxuryMixin import LuxuryMixin

class ElectricCar(Car, ElectricMixin, LuxuryMixin):
    def __init__(self, license_plate: str, year: int, engine: Engine):
        super().__init__(license_plate, year, engine)

    def calculate_annual_tax(self):
        return 250