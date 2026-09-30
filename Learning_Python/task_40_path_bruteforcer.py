"""টাস্ক: ওয়েবসাইটে লুকানো বা সংবেদনশীল পাথ আছে কি না তা খোঁজার একটি সাধারণ ডিরেক্টরি ব্রুটফোর্স স্ক্রিপ্ট বানাও।

একটি বেস URL নাও: base_url = "[https://httpbin.org](https://httpbin.org)"

সাধারণ কিছু পাথের একটি লিস্ট তৈরি করো: paths = ["/admin", "/login", "/status/404", "/status/200", "/hidden"]

লুপ চালিয়ে প্রতিটি পাথের সাথে base_url জোড়া লাগিয়ে (যেমন: [https://httpbin.org/login](https://httpbin.org/login)) রিকোয়েস্ট পাঠাও।

শুধু যে পাথগুলোতে স্ট্যাটাস কোড 200 (Found/OK) ফেরত আসে, সেগুলোকে স্ক্রিনে প্রিন্ট করে দেখাও: [+] Found valid path: {full_url}।"""

import requests

base_url = "https://httpbin.org"
paths = ["/admin", "/login", "/status/404", "/status/200", "/hidden"]

for path in paths:
    full_url = f"{base_url}{path}"

    try:
        response = requests.get(full_url, timeout=3)
        if response.status_code == 200:
            print (f"[+] Found valid path (200 OK): {full_url}")
        else:
            print(f"[-] Status {response.status_code}: {path}")

    except requests.exceptions.RequestException as e:
        print(f"[-] Error connecting to: {full_url}")