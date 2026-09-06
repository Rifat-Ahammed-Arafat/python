"""টাস্ক: Car নামে একটি ক্লাস বানাও যার ভেতর brand, model, এবং year থাকবে (__init__ এর মাধ্যমে)।

ক্লাসের ভেতর একটি মেথড থাকবে car_details() যা গাড়ির সম্পূর্ণ তথ্য প্রিন্ট করবে।

দুটি আলাদা গাড়ির অবজেক্ট তৈরি করে তাদের মেথড কল করে আউটপুট দেখো।"""

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