"""টাস্ক: ইউজার থেকে একটি সংখ্যা ইনপুট নেবে (যেমন: 5)। while loop ব্যবহার করে সংখ্যাটি থেকে ১ পর্যন্ত উল্টো কাউন্টডাউন করবে এবং লুপ শেষ হলে নিচে Blast off! প্রিন্ট করবে।

আউটপুট কেমন হবে (ইউজার ৫ দিলে):
5
4
3
2
1
Blast off!"""

num = int (input("Enter a number:"))

while num >= 1:
    print (num)
    num -= 1
print ("Blast off!")