# --- 1. Polymorphism (Method Overriding) ---
class Animal :
    def make_sound(self):
        print ("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog says : Woof! Woof!")

class Cat (Animal):
    def make_sound(self):
        print ("Cat says : Meow!")


dog = Dog()
cat = Cat()
dog.make_sound()
cat.make_sound()


# --- 2. Encapsulation (Private Attributes) ---
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def get_balance(self):
        return f"Current balance: {self.__balance}"

    def deposit(self, amount):
        if amount > 0:
            self.__balance = amount
            print (f"Deposited ${amount} successfully.")
        else:
            print ("Invalid deposit amount!")


account = BankAccount("Rifat", 1000)

print (account.get_balance())
account.deposit(500)
print(account.get_balance())