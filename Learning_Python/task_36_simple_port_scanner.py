"""টাস্ক: ইউজার থেকে একটি টার্গেট হোস্ট ইনপুট নাও (টেস্টের জন্য scanme.nmap.org বা লোকালহোস্ট 127.0.0.1 ব্যবহার করতে পারো)।

এরপর একটি for লুপ ব্যবহার করে 20 থেকে 85 পর্যন্ত পোর্টগুলো স্ক্যান করো।

লুপের ভেতর প্রতিটি পোর্টে সকেট কানেক্ট করে শুধু যে পোর্টগুলো OPEN (result == 0), সেগুলোর তালিকা স্ক্রিনে প্রিন্ট করো।"""

import socket

target_host = input("Enter a host: ")

try:
    target_ip = socket.gethostbyname(target_host)
    print (f"Scanning target: {target_host} ({target_ip})\n") 
except socket.gaierror:
    print (f"[Error] Could not resolve host {target_host}")
    exit()
print ("Open ports found: ")
for port in range (20, 86):
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)

    result = s.connect_ex ((target_ip, port))
    if result == 0 :
        print (f"[+] Port {port} is OPEN")
    s.close()