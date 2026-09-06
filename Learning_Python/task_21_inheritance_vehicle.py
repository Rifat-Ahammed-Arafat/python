"""টাস্ক: একটি প্যারেন্ট ক্লাস বানাও Vehicle যার ভেতর brand এবং speed থাকবে এবং একটি মেথড drive() থাকবে যা প্রিন্ট করবে Driving at {speed} km/h।

এবার একটি চাইল্ড ক্লাস বানাও ElectricCar যা Vehicle কে ইনহেরিট করবে এবং এতে অতিরিক্ত battery_capacity থাকবে।

ElectricCar-এর একটি অবজেক্ট বানিয়ে drive() মেথড এবং ব্যাটারি ক্যাপাসিটি প্রিন্ট করে দেখাও।"""

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