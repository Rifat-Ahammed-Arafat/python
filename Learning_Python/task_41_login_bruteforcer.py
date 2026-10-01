"""টাস্ক: একটি সিম্পল পাসওয়ার্ড ক্র্যাকিং / ব্রুটফোর্স সিমুলেশন তৈরি করো।

টার্গেট URL: url = "[https://httpbin.org/post](https://httpbin.org/post)"

একটি ইউজারনেম রাখো: username = "admin"

সাধারণ কয়েকটি পাসওয়ার্ডের একটি লিস্ট তৈরি করো: password_list = ["123456", "password", "admin123", "secret2026", "toor"]

একটি লুপ চালিয়ে প্রতিটি পাসওয়ার্ড দিয়ে requests.post() রিকোয়েস্ট পাঠাও।

ধরে নাও সঠিক পাসওয়ার্ডটি হলো "secret2026"। যদি রেসপন্সের ভেতর এই পাসওয়ার্ডটি থাকে (বা তুমি কন্ডিশন দিয়ে ম্যাচ করাও), তবে প্রিন্ট করবে:
[+] SUCCESS! Password found: {password} এবং লুপ থেকে break করে বের হয়ে যাবে।

ভুল পাসওয়ার্ড হলে প্রিন্ট করবে: [-] Trying {password}... Failed।"""

import requests

target_url = "https://httpbin.org/post"

username = "admin"
password_list = ["123456", "password", "admin123", "secret2026", "toor"]

for password in password_list:
    payload = {
        "username" : username,
        "password" : password
    }
    try:
        response = requests.post(target_url, data=payload, timeout=5)

        if password == "secret2026":
            print(f"[+] SUCCESS! Password found: {password}")
            break
        else:
            print(f"[-] Trying {password}... Failed")

    except requests.exceptions.RequestException as e:
        print(f"[-] Connection Error: {e}")