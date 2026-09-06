"""টাস্ক: ইউজার থেকে একটি পূর্ণসংখ্যা ইনপুট নেবে। for loop ব্যবহার করে সেই সংখ্যার নামতা (Multiplication Table) ১ থেকে ১০ পর্যন্ত সুন্দর করে প্রিন্ট করবে।

আউটপুট কেমন হবে (ইউজার ৫ দিলে):
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50"""

num = int (input ("Enter a number :"))

for i in range (1 , 11):
    print (f"{num} x {i} = {num*i}")