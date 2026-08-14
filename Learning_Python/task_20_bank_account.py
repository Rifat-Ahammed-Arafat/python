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