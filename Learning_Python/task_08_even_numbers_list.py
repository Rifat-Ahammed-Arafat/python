"""টাস্ক: একটি খালি লিস্ট তৈরি করো my_list = [] । ইউজার থেকে for loop ব্যবহার করে ৫টি সংখ্যা ইনপুট নাও এবং append() দিয়ে লিস্টে জমা করো। এরপর লিস্টের ভেতরে শুধু যে সংখ্যাগুলো জোড় (Even), সেগুলোকে স্ক্রিনে প্রিন্ট করে দেখাও।"""

my_list = []

for i in range (1, 6):
    num = int (input("Enter a number: "))
    my_list.append(num)
print (f"Full list: {my_list}")


print (f"Even numbers on the list : ")
for num in my_list:
    if num % 2 == 0 :
        print (num)
