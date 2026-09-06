"""টাস্ক: try-except ব্যবহার করে random_data.txt নামের একটি ফাইল ওপেন করে পড়ার চেষ্টা করো। ফাইলটি যদি না থাকে, তবে পাইথন যেন ক্র্যাশ না করে FileNotFoundError হ্যান্ডেল করে মেসেজ দেয়: File does not exist!।"""

try:
    with open("random_data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print ("File does not exist!")
finally:
    print ("Execution completed.")