def greet ():
    print ("Hello! Welcome to Python class.")
greet()

def greet_user(username):
    print (f"Hello, {username}! Hope you are during well.")
greet_user("Rifat")

def add_numbers(num1, num2):
    sum_result = num1 + num2
    return sum_result

total = add_numbers(15, 25)
print (f"total sum : {total}")