"""টাস্ক: সপ্তাহের ৭ দিনের নাম দিয়ে একটি টুপল বানাও (days = ("Saturday", "Sunday", ...) । ইউজার থেকে ১ থেকে ৭ এর মধ্যে যেকোনো একটি সংখ্যা ইনপুট নাও এবং সেই দিনটির নাম স্ক্রিনে প্রিন্ট করো। (যেমন: ইউজার ১ দিলে Saturday প্রিন্ট হবে, ২ দিলে Sunday)।"""

days = ("Saturday", "Sunday", "Monday" , "Tuesday", "Wednesday", "Thursday", "Friday")

num = int (input ("Enter a number from 1 to 7: "))
selected_day = days[num-1]
print (f"Day {num} is {selected_day}")


