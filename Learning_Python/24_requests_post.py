import requests

login_url = "https://httpbin.org/post"

payload = {
    "username": "admin",
    "password": "secret_password"
}

response = requests.post(login_url, data=payload, timeout=5)

print(f"Status Code: {response.status_code}")
print("Server received data:")
print(response.json().get("form"))