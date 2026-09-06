"""টাস্ক: একটি ফাংশন বানাও calculate_square(number) নামে। এটি একটি সংখ্যা ইনপুট নেবে এবং সংখ্যাটির বর্গ (Square) রিটার্ন করবে। এরপর ইউজার থেকে ইনপুট নিয়ে ফাংশনটিকে কল করে বর্গ প্রিন্ট করে দেখাও।"""

def calculate_square(number):
    square = number ** 2
    return  square

number = int(input("Enter a number: "))

squared_value = calculate_square(number)
print (f"Square of {number}: {squared_value}")
