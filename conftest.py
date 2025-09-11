import os
import uuid
import requests
import pytest
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:5000")

def _extract_token(json_data):
    """Try common keys to find a JWT token, fallback detect a JWT-like string."""
    if not isinstance(json_data, dict):
        return None
    for key in ("token", "access_token", "accessToken", "jwt"):
        if key in json_data:
            return json_data[key]
    # fallback: look for any string value that looks like a JWT (three parts separated by '.')
    for v in json_data.values():
        if isinstance(v, str) and v.count('.') == 2:
            return v
    return None

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL.rstrip('/')

@pytest.fixture(scope="session")
def auth_token(base_url):
    """Ensure test user exists, then log in and return JWT token."""
    username = f"testuser_{uuid.uuid4().hex[:8]}"
    password = "Password123!"
    payload = {"username": username, "password": password}

    # Signup first
    signup_res = requests.post(f"{base_url}/signup", json=payload, timeout=5)
    assert signup_res.status_code in (200, 201), f"Signup failed: {signup_res.status_code} {signup_res.text}"

    # Login to get JWT
    login_res = requests.post(f"{base_url}/login", json=payload, timeout=5)
    assert login_res.status_code == 200, f"Login failed: {login_res.status_code} {login_res.text}"

    token = _extract_token(login_res.json())
    assert token, f"Token not found in login response: {login_res.text}"

    return token
