"""কাজ: SSH ক্লায়েন্ট তৈরি করা এবং রিমোট মেশিনে কমান্ড এক্সিকিউট করা।
"""

import paramiko

# SSH ক্লায়েন্ট ইনিশিয়ালাইজ করা
ssh = paramiko.SSHClient()

# সার্ভারের হোস্ট-কি (Host Key) আগে থেকে সেভ না থাকলেও অটোমেটিক যুক্ত করবে
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# রিমোট সার্ভারের তথ্য (টেস্টিং ডামি ডাটা)
host = "127.0.0.1"
port = 22
username = "testuser"
password = "testpassword"

try:
    print(f"[*] Connecting to {host}:{port} via SSH...")
    # সার্ভারে কানেক্ট করার মেথড
    ssh.connect(hostname=host, port=port, username=username, password=password, timeout=5)
    print("[+] SSH Connection Established Successfully!")

    # রিমোট সার্ভারে কমান্ড চালানো
    # exec_command() তিনটি স্ট্রিম রিটার্ন করে: stdin, stdout, stderr
    stdin, stdout, stderr = ssh.exec_command("whoami")

    # আউটপুট রিড করা
    output = stdout.read().decode().strip()
    errors = stderr.read().decode().strip()

    if output:
        print(f"[+] Output: {output}")
    if errors:
        print(f"[-] Error Output: {errors}")

except paramiko.AuthenticationException:
    print("[-] Authentication Failed! Incorrect username or password.")
except paramiko.SSHException as e:
    print(f"[-] SSH Error: {e}")
except Exception as e:
    print(f"[-] Connection Failed: {e}")

finally:
    # কাজ শেষ হলে সেশন ক্লোজ করা
    ssh.close()
    print("[*] SSH connection closed.")


"""লক্ষণীয় বিষয়:

AutoAddPolicy(): কানেক্ট করার সময় "Are you sure you want to continue connecting (yes/no)?" এই প্রম্পটটি বাইপাস করতে সাহায্য করে।

stdout.read().decode(): সার্ভারে চলা কমান্ডের আউটপুট বাইট থেকে টেক্সটে কনভার্ট করে আনে।

AuthenticationException: পাসওয়ার্ড ভুল হলে এই নির্দিষ্ট এক্সেপশনটি ট্রিগার হয়।"""