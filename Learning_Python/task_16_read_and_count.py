"""টাস্ক: user_data.txt ফাইলটি রিড (r মোড) করো। ফাইলের ভেতরে মোট কতটি অক্ষর (character) আছে তা গুনে স্ক্রিনে প্রিন্ট করে দেখাও। (হিন্ট: len() ফাংশন ব্যবহার করতে পারো)।"""

with open ("user_data.txt", "r") as file:
    content = file.read()
    total_characters = len(content)
    print (f"File content: \n{content}")
    print (f"Total characters in that file : {total_characters}")