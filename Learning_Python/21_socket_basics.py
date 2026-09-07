"""কাজ: ডোমেন নেম থেকে আইপি অ্যাড্রেস বের করা এবং একটি নির্দিষ্ট আইপি ও পোর্টে টিসিপি কানেকশন চেক করা।"""

import socket


target_host = "scanme.nmap.org"

try:
    target_ip = socket.gethostbyname(target_host)
    print (f"Target Host: {target_host}")
    print (f"Resolved IP Address: {target_ip}")
except socket.gaierror:
    print(f"[Error] Could not resolve host {target_host}")
    exit()

port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.settimeout(2.0)

result = s.connect_ex((target_ip , port))

if result == 0 :
    print (f"[+] Port {port} is OPEN on {target_ip}")
else :
    print (f"[-] Port {port} is CLOSED or filtered")

s.close()
