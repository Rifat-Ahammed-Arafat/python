class Vehicle :
    def __init__(self, brand , speed):
        self. brand = brand
        self.speed = speed

    def drive(self):
        print (f"Driving at {self.speed} km/h")


class ElectricCar(Vehicle):
    def __init__(self, brand, speed, battery_capacity):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity

car = ElectricCar("BMW", 150, "5000 kWh")
car.drive()
print (f"Battery capacity : {car.battery_capacity}")