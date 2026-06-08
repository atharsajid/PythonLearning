
#Class Method and Self 

class Car:
    total_car = 0 #To keep record how many instance have been created
    def __init__(self, brand, model):
        self.__brand = brand ##__ use to make variable private
        self.__model = model
        # self.total_car += 1 #Method 1
        Car.total_car += 1 #Method 2
     
    #Getter 
    def get_brand(self):
        return self.__brand + "!"
    
    #Setter
    def set_brand(self, brand):
        self.__brand = brand

    def fullName(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property #To Make variable read only
    def model(self):
        return self.__model


my_car = Car("Toyota", "2024")

print("I have", my_car.get_brand(), my_car.model)

print(my_car.fullName())
print(my_car.fuel_type())

#Inheritance

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"
    

my_electric_car = ElectricCar("EV", "2026", "50kW")
my_electric_car.set_brand("Tesla")
print(my_electric_car.get_brand())
print(my_electric_car.fuel_type())

print(Car.total_car)

#Check instance of Class
print(isinstance(my_electric_car, Car))
print(isinstance(my_electric_car, ElectricCar))

# my_electric_car = ElectricCar("EV", "2026", "50kW")
# my_electric_car.brand = "Tesla"
# name = f"{my_electric_car.brand} {my_electric_car.model} {my_electric_car.battery_size}"

# print(name)


my_car = Car("Honda", "2026")

print(Car.general_description())