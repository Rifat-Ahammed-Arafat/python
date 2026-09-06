"""টাস্ক: math মডিউল ব্যবহার করে ইউজার থেকে একটি সংখ্যা ইনপুট নাও এবং সেই সংখ্যার বর্গমূল (math.sqrt) এবং ফ্যাক্টোরিয়াল (math.factorial) বের করে প্রিন্ট করো।"""
import math

num = int(input ("Enter a number : "))

sqrt = math.sqrt(num)
print (f"The square root of {num} is {sqrt}")

fact = math.factorial(num)
print (f"The facotrial of {num} is {fact}")