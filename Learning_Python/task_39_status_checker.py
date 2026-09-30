"""টাস্ক: ইউজার থেকে একটি ওয়েবসাইটের URL ইনপুট নাও (যেমন: [https://google.com](https://google.com) বা [https://github.com](https://github.com))।

requests.get() ব্যবহার করে ওয়েবসাইটের Status Code এবং Server Header বের করে প্রিন্ট করো।

যদি স্ট্যাটাস কোড ২০০ হয়, তবে প্রিন্ট করবে [+] Website is UP & reachable, অন্যথায় প্রিন্ট করবে [-] Warning: Status code {code}।"""

import requests

url = input ("Enter an url: ")
try:
    response = requests.get(url, timeout=5)

    print(f"[+] Status code: {response.status_code}")

    print("\n--- Response Headers ---")
    server_info = response.headers.get("Server", "Unknown")
    content_type = response.headers.get("Content-Type", "Unknown")
    print(f"Server technology: {server_info}")
    print(f"Content Type: {content_type}")


    code = response.status_code
    if code == 200:
        print("[+] Website is UP & reachable")
    else:
        print(f"[-] Warning: Status code {code}")

except requests.exceptions.Timeout:
    print(f"[Request timed out!]")
except requests.exceptions.RequestException as e:
    print(f"[-] An error occurred: {e}")