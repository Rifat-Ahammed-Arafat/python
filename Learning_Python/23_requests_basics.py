"""কাজ: HTTP GET রিকোয়েস্ট পাঠানো, স্ট্যাটাস কোড ও হেডার থেকে ওয়েব সার্ভারের তথ্য রিড করা।"""

import requests

url = "https://httpbin.org/get"

try:
    response = requests.get(url, timeout=5)

    print(f"[+] Status Code: {response.status_code}")

    print("\n--- Response Headers ---")
    server_info = response.headers.get("Server", "Unknown")
    Content_type = response.headers.get("Content-Type", "Unknown")
    print(f"Server technology: {server_info}")
    print (f"Content type: {Content_type}")

    print("\n--- Response Body Preview ---")
    print(response.text[:200])

except requests.exceptions.Timeout:
    print("[-] Request timed out!")
except requests.exceptions.RequestException as e:
    print(f"[-] An error occurred: {e}")


"""লক্ষণীয় বিষয়:

response.status_code: সার্ভারের রেসপন্স কোড দেয় (যেমন 200, 301, 403, 404, 500)।

response.headers: সার্ভার থেকে আসা সব সিকিউরিটি হেডার একটি পাইথন ডিকশনারি আকারে ফেরত দেয়।

response.text: ওয়েবসাইটের HTML বা JSON আউটপুট দেয়।"""