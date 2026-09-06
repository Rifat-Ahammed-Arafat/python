"""টাস্ক: BankAccount নামে একটি ক্লাস তৈরি করো যার ভেতর account_holder এবং balance থাকবে।

ক্লাসের ভেতর দুটি মেথড থাকবে:

deposit(amount): অ্যাকাউন্টে টাকা জমা করবে এবং নতুন ব্যালেন্স প্রিন্ট করবে।

check_balance(): বর্তমান ব্যালেন্স দেখাবে।

একটি অবজেক্ট বানিয়ে টাকা জমা করে ব্যালেন্স চেক করো।"""

class BankAccount :
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print (f"Deposited: ${amount}. New balance: ${self.balance}")

    def check_balance(self):
        print (f"Account holder: {self.account_holder} | Balance : {self.balance}")

my_acc = BankAccount("Rifat", 500)
my_acc.check_balance()
my_acc.deposit(200)