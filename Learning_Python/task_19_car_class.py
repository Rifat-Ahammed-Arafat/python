class Car:
    def __init__(self, brand, model , year):
        self. brand = brand
        self.model = model
        self.year = year

    def car_details(self):
        print (f"Car Information : {self.brand} | {self.model} | {self.year}")

car1 = Car("BMW", "Wagons" , 1990)
car2 = Car("Ferrari", "Ferrari Luce" , 1995)

car1.car_details()
car2.car_details()