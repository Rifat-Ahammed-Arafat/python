"""টাস্ক: একটি ফাংশন বানাও find_max(a, b) নামে। এটি দুটি সংখ্যা ইনপুট হিসেবে নেবে এবং দুটির মধ্যে যেটি বড় সেটি রিটার্ন করবে। ফাংশনটি কল করে বড় সংখ্যাটি প্রিন্ট করে দেখাও।"""

def find_max(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else: return a

a = int (input("Enter a number : "))
b = int (input("Enter another number : "))


max_value = find_max(a, b)
print (f"Max value is : {max_value}") 
    