"""টাস্ক: ATMCard নামে একটি ক্লাস তৈরি করো যার ভেতরে card_number এবং একটি প্রাইভেট ভেরিয়েবল __pin থাকবে।

একটি মেথড বানাও change_pin(old_pin, new_pin)। যদি ইউজার সঠিক old_pin দেয়, তবেই পিন পরিবর্তন হবে এবং প্রিন্ট করবে PIN changed successfully!, ভুল পিন দিলে প্রিন্ট করবে Incorrect current PIN!।"""

class ATMCard:
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.__pin = pin

    def change_pin (self, old_pin , new_pin):
        if old_pin == self.__pin:
            self.__pin == new_pin
            print ("PIN changed successfully!")
        else:
            print ("Incorrect current PIN! Access denied.")


my_card = ATMCard ("1234-5678-9012", 1122)
my_card.change_pin(9999, 4321) #wrong current pin
my_card.change_pin(1122, 4321) #correct current pin