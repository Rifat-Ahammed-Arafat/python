"""টাস্ক: ইউজার থেকে একটি টার্গেট আইপি/হোস্ট এবং একটি পোর্ট নম্বর ইনপুট নাও। এরপর socket ব্যবহার করে চেক করো সেই পোর্টটি ওপেন আছে কি না। ফলাফল সুন্দরভাবে প্রিন্ট করে দেখাও এবং কাজ শেষে সকেট ক্লোজ করো।"""

import socket

target_host = input("Enter a host: ")
port = int(input("Enter a port number: "))

try:
    target_ip = socket.gethostbyname(target_host)
    print (f"Target Host: {target_host}")
    print (f"Resolved IP Address: {target_ip}")
except socket.gaierror:
    print (f"[Error] Could not resolve host {target_host}")
    exit()

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2.0)

result = s.connect_ex ((target_ip, port))
if result == 0 :
    print (f"[+] Port {port} is OPEN on {target_ip}")
else :
    print (f"[-] Port {port} is CLOSED or Filtered")

s.close()