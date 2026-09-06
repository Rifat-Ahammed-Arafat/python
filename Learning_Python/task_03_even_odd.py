"""টাস্ক: ইউজার থেকে একটি পূর্ণসংখ্যা (int) ইনপুট নেবে। সংখ্যাটি জোড় (Even) নাকি বিজোর (Odd) তা বের করে প্রিন্ট করবে। (হিন্ট: জোড় সংখ্যাকে ২ দিয়ে ভাগ করলে ভাগশেষ % সবসময় ০ হয়)।"""

num = int (input("Enter a number : "))

if num % 2 == 0 :
    print (f"{num} is a even number.")
else: 
    print (f"{num} is an odd number.")