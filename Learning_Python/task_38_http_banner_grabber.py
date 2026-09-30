"""টাস্ক: পোর্ট 80 (HTTP)-তে কানেক্ট করো। কানেক্ট করার পর s.send(b"HEAD / HTTP/1.1\r\nHost: scanme.nmap.org\r\n\r\n") কমান্ড পাঠিয়ে সার্ভার থেকে রেসপন্স রিসিভ (s.recv(1024)) করো এবং প্রিন্ট করো। এতে সার্ভারের HTTP হেডার ও ওয়েব সার্ভারের তথ্য দেখতে পাবে।"""

import socket

target_host = "scanme.nmap.org"
port = 80

try:
    target_ip = socket.gethostbyname(target_host)
    print (f"Connecting to {target_host} {target_ip} on port {port}")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3.0)
    s.connect((target_ip, port))

    s.send(b"HEAD / HTTP/1.1\r\nHost:scanme.nmap.org\r\n\r\n")
    banner = s.recv(1024).decode().strip()
    print(f"[+] Service banner: {banner}")

except socket.timeout:
    print (f"[-] Connection timed out on port {port}")
except Exception as e:
    print (f"[-] Cound not grab banner : {e}")
