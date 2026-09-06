"""টাস্ক: ইউজার থেকে দুটি সংখ্যা ইনপুট নেবে।

যদি প্রথম সংখ্যাটি বড় হয়, প্রিন্ট করবে: First number is larger

যদি দ্বিতীয় সংখ্যাটি বড় হয়, প্রিন্ট করবে: Second number is larger

আর যদি দুটি সংখ্যাই সমান হয়, প্রিন্ট করবে: Both numbers are equal"""

num1 = int (input ("Enter first number :"))
num2 = int (input ("Enter second number :"))

if num1 > num2 :
    print ("First number is larger.")
elif num1 < num2 :
    print ("Second number is larger.")
else :
    print ("Both numbers are equal.")
