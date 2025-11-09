class Engine:
    def __init__(self, horsepower: int, fuel_type: str):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def __str__(self):
        return f"Engine({self.horsepower} HP, {self.fuel_type})"