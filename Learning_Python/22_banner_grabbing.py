"""কাজ: কোনো পোর্টে কানেক্ট করে সার্ভিসের ব্যানার রিড করা।"""

import socket

target_host = "scanme.nmap.org"
port = 22

try :
    target_ip = socket.gethostbyname(target_host)
    print (f"Connecting to {target_host} {target_ip} on port {port}")
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3.0)
    s.connect((target_ip, port))
    
    banner = s.recv(1024).decode().strip()
    print(f"[+] Service banner: {banner}")
    
    s.close()
    
except socket.timeout:
    print(f"[-] Connection timed out on port {port}")
except Exception as e :
    print(f"[-] Could not grab banner: {e}")
