"""টাস্ক: ইউজার থেকে একটি পূর্ণসংখ্যা ইনপুট নেওয়ার চেষ্টা করো। ইউজার যদি সংখ্যার জায়গায় কোনো লেখা (টেক্সট) দিয়ে দেয়, যেন প্রোগ্রাম ক্র্যাশ না করে স্ক্রিনে প্রিন্ট করে: Please enter a valid integer!।"""

try :
    num = int (input ("Enter an integer: "))
    print (f"The integer is : {num}")
except ValueError:
    print ("Please enter a valid integer!")
finally :
    print ("Execution completed.")