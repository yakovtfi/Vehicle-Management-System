from classes.engine import Engine
from classes.car import Car
from classes.truck import Truck
from classes.electricCar import ElectricCar

if __name__ == "__main__":

    engine1 = Engine(120, "Petrol")
    engine2 = Engine(450, "Diesel")
    engine3 = Engine(200, "Electric")


    car = Car("45-345-67", 2012, engine1)
    truck = Truck("98-765-32", 2025, max_load=8000)
    ecar = ElectricCar("11-222-33", 2024, engine3)

    vehicles = [car, truck, ecar]

    print("\n ____Annual Tax Calculation (Polymorphism Demo)______ ")
    for v in vehicles:
        print(f"{v.__class__.__name__} [{v.get_license_plate()}]: {v.calculate_annual_tax()} ₪")

    print("\n____Encapsulation Demo____ ")
    print("Old license plate:", car.get_license_plate())
    car.set_license_plate("95-222-73")
    print("Updated license plate:", car.get_license_plate())

    print("\n____Multiple Inheritance (Mixins) Demo____")
    ecar.charge()
    print("Luxury features:", ecar.get_luxury_features())