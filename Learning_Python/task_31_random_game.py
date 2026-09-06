"""টাস্ক: random মডিউল ব্যবহার করে কম্পিউটার ১ থেকে ১০ এর মধ্যে একটি গোপন সংখ্যা তৈরি করবে (random.randint(1, 10))। ইউজার থেকে একটি সংখ্যা ইনপুট নাও। ইউজারের সংখ্যা আর কম্পিউটারের গোপন সংখ্যা মিলে গেলে প্রিন্ট করো: You Win! 🎉, না মিললে প্রিন্ট করো: Wrong guess! The number was X।"""


import random

secret_number = random.randint(1, 10)

num = int (input ("Enter a number : "))


if secret_number == num :
    print ("You win!")
else:
    print (f"Wrong guess the number was {secret_number}")