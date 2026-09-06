import math 
import random
import datetime
import os

print (f"Square root of 64 : {math.sqrt(64)}")
print (f"Factorial of 5 : {math.factorial(5)}")
print(f"Value of PI : {math.pi}")

secret_number = random.randint(1, 10)
print (f"Randor number : {secret_number}")

colors = ["Red" , "Green", "Blue" , "Yellow"]
chosen_color = random.choice(colors)
print (f"Random choice: {chosen_color}")

current_time = datetime.datetime.now()
print (f"Current Date and Time : {current_time.strftime("%Y-%m-%d %H:%M:%S")}")

print (f"Current Directory: {os.getcwd()}")
