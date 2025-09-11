# tests/test_auth.py
import uuid
import requests

def test_signup_and_login(base_url):
    username = f"tmp_{uuid.uuid4().hex[:6]}"
    password = "Passw0rd!"
    signup = requests.post(f"{base_url}/signup", json={"username": username, "password": password})
    assert signup.status_code in (200, 201, 400)  # 400 if already exists; unlikely with unique username

    login = requests.post(f"{base_url}/login", json={"username": username, "password": password})
    assert login.status_code == 200
    data = login.json()
    # token may be under 'token' or 'access_token' etc.
    token = None
    for k in ("token", "access_token", "accessToken", "jwt"):
        if k in data:
            token = data[k]
            break
    assert token or any(isinstance(v, str) and v.count('.') == 2 for v in data.values()), "No JWT token found"
