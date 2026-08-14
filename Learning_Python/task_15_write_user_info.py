name = input ("Enter your name : ")
email = input ("Enter your email : ")

with open ("user_data.txt", "w") as file:
    file.write (f"{name}\n")
    file.write (f"{email}\n")