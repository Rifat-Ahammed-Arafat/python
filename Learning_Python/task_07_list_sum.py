"""টাস্ক: ৫টি সংখ্যার একটি লিস্ট বানাও (যেমন: numbers = [10, 20, 30, 40, 50])। for loop ব্যবহার করে লিস্টের সবকটি সংখ্যার যোগফল বের করে স্ক্রিনে প্রিন্ট করো। (হিন্ট: লুপের বাইরে total = 0 দিয়ে শুরু করতে পারো)।"""

numbers = [10, 20, 30, 40, 50]

total=0
for number in numbers:
    total = total + number
print (f"Total sum: {total}")
