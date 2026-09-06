"""টাস্ক: ইউজার থেকে for loop দিয়ে ৫টি সংখ্যা ইনপুট নিয়ে একটি লিস্টে রাখো। ইউজার যদি একই সংখ্যা বারবার ইনপুট দেয়, তবে Set ব্যবহার করে সেই লিস্ট থেকে ডুপ্লিকেট সংখ্যাগুলো বাদ দিয়ে ইউনিক সংখ্যার লিস্টটি স্ক্রিনে প্রিন্ট করো।"""

numbers = []

for num in range (1,6):
    num = int (input(f"Enter a number {num}: "))
    numbers.append(num)
print (f"List: {numbers}")

unique_list = list(set(numbers))
print (f"Unique list (No Duplicates): {unique_list}")







