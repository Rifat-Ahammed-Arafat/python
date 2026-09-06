"""টাস্ক:

একটি Lambda ফাংশন বানাও যা দুটি সংখ্যার গুণফল রিটার্ন করবে।

আরেকটি Lambda ফাংশন বানাও যা একটি স্ট্রিং (টেক্সট) ইনপুট নিলে তার দৈর্ঘ্য (len()) রিটার্ন করবে।

দুটি ফাংশন কল করে প্রিন্ট দিয়ে আউটপুট দেখো।"""

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
mul = lambda num1 , num2 : num1 * num2

print (f"Multiplication is : {mul(num1, num2)}")


string = input ("Enter a string: ")
string_len = lambda string : len(string)


print (f"String length is : {string_len(string)}")