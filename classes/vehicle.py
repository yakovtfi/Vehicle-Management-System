from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, license_plate: str, year: int):
        self.__license_plate = license_plate
        self.__year = year


    def get_license_plate(self):
        return self.__license_plate

    def get_year(self):
        return self.__year


    def set_license_plate(self, new_plate: str):
        print(f"Changing license plate from {self.__license_plate} to {new_plate}")
        self.__license_plate = new_plate

    def set_year(self, new_year: int):
        print(f"Changing year from {self.__year} to {new_year}")
        self.__year = new_year

    @abstractmethod
    def calculate_annual_tax(self):
        pass