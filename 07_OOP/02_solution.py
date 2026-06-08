from solution import Car

class Battery:
    def battery_info(self):
        return "50 KWH Battery"

class Engine:
    def engine_info(self):
        return "This is Engine"

class ElectricCar(Battery, Engine, Car):
    pass


my_tesla = ElectricCar(brand= "Honda", model= "2025")

print(my_tesla.fullName())
print(my_tesla.battery_info())
print(my_tesla.engine_info())