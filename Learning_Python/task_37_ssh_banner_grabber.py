"""টাস্ক: ইউজার থেকে একটি হোস্ট ইনপুট নাও। পোর্ট 22 (SSH)-এ কানেক্ট করে সার্ভারের ব্যানারটি রিড করো। যদি কোনো ব্যানার আসে, সেটি সুন্দর করে স্ক্রিনে প্রিন্ট করো। টাইমআউট বা কানেকশন ফেইল হলে try-except দিয়ে এরর হ্যান্ডেল করো। (টেস্ট করার জন্য scanme.nmap.org ব্যবহার করতে পারো)।"""

import socket

target_host = input("Enter a host: ")
port = 22

try :
    target_ip = socket.gethostbyname(target_host)
    print (f"Connecting to {target_host} {target_ip} on port {port}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3.0)
    s.connect((target_ip, port))

    banner = s.recv(1024).decode().strip()
    print(f"[+] Service banner : {banner}")

    s.close()
except socket.timeout:
    print(f"[-] Connection timed out on port {port}")
except Exception as e:
    print(f"[-] Could not grab banner: {e}")