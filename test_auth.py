import requests

BASE = "http://localhost:8000"

# 1. Signup
r = requests.post(f"{BASE}/auth/signup", json={
    "email": "test2@example.com",
    "password": "AnotherPass123"
})
print("Signup:", r.status_code, r.json())

# 2. Login
r = requests.post(f"{BASE}/auth/login", data={
    "username": "test2@example.com",
    "password": "AnotherPass123"
})
print("Login:", r.status_code, r.json())
token = r.json()["access_token"]

# 3. Me
r = requests.get(f"{BASE}/auth/me", headers={"Authorization": f"Bearer {token}"})
print("Me:", r.status_code, r.json())
