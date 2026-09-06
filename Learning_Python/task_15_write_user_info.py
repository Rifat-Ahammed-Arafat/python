"""টাস্ক: ইউজার থেকে তার নাম ও ইমেইল ইনপুট নাও। এরপর user_data.txt নামে একটি ফাইলে সেই নাম ও ইমেইল সুন্দর করে সেভ করো (w মোড দিয়ে)।"""

name = input ("Enter your name : ")
email = input ("Enter your email : ")

with open ("user_data.txt", "w") as file:
    file.write (f"{name}\n")
    file.write (f"{email}\n")