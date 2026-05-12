"""
auth.py - User Authentication Module
Features: register, login, logout, password hashing, session management
"""

import hashlib
import hmac
import os
import json
import time
from datetime import datetime


# ---------------------------------------------------------------------------
# Password Utilities
# ---------------------------------------------------------------------------

def hash_password(password: str) -> tuple[str, str]:
    """Hash a password with a random salt. Returns (salt, hashed_password)."""
    salt = os.urandom(32).hex()
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        100000
    )
    return salt, key.hex()


def verify_password(password: str, salt: str, hashed: str) -> bool:
    """Verify a password against its salt and hash."""
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        100000
    )
    return hmac.compare_digest(key.hex(), hashed)


# ---------------------------------------------------------------------------
# User Store (in-memory)
# ---------------------------------------------------------------------------

class UserStore:
    """Simple in-memory user database."""

    def __init__(self):
        self._users: dict[str, dict] = {}

    def add_user(self, username: str, salt: str, hashed: str, email: str) -> None:
        self._users[username] = {
            'username': username,
            'email': email,
            'salt': salt,
            'hashed': hashed,
            'created_at': datetime.utcnow().isoformat(),
            'is_active': True
        }

    def get_user(self, username: str) -> dict | None:
        return self._users.get(username)

    def user_exists(self, username: str) -> bool:
        return username in self._users

    def deactivate_user(self, username: str) -> bool:
        if username in self._users:
            self._users[username]['is_active'] = False
            return True
        return False


# ---------------------------------------------------------------------------
# Session Manager
# ---------------------------------------------------------------------------

class SessionManager:
    """Manages active user sessions with expiry."""

    SESSION_TTL = 3600  # 1 hour

    def __init__(self):
        self._sessions: dict[str, dict] = {}

    def create_session(self, username: str) -> str:
        token = os.urandom(32).hex()
        self._sessions[token] = {
            'username': username,
            'created_at': time.time(),
            'expires_at': time.time() + self.SESSION_TTL
        }
        return token

    def validate_session(self, token: str) -> str | None:
        session = self._sessions.get(token)
        if not session:
            return None
        if time.time() > session['expires_at']:
            del self._sessions[token]
            return None
        return session['username']

    def delete_session(self, token: str) -> bool:
        if token in self._sessions:
            del self._sessions[token]
            return True
        return False

    def active_sessions(self) -> int:
        return len(self._sessions)


# ---------------------------------------------------------------------------
# Auth Service
# ---------------------------------------------------------------------------

class AuthService:
    """Main authentication service combining UserStore and SessionManager."""

    def __init__(self):
        self.users = UserStore()
        self.sessions = SessionManager()

    def register(self, username: str, password: str, email: str) -> dict:
        if not username or not password or not email:
            return {'success': False, 'error': 'All fields are required'}
        if len(username) < 3:
            return {'success': False, 'error': 'Username must be at least 3 characters'}
        if len(password) < 8:
            return {'success': False, 'error': 'Password must be at least 8 characters'}
        if '@' not in email:
            return {'success': False, 'error': 'Invalid email address'}
        if self.users.user_exists(username):
            return {'success': False, 'error': 'Username already exists'}
        salt, hashed = hash_password(password)
        self.users.add_user(username, salt, hashed, email)
        return {'success': True, 'message': f"User '{username}' registered successfully"}

    def login(self, username: str, password: str) -> dict:
        user = self.users.get_user(username)
        if not user:
            return {'success': False, 'error': 'Invalid username or password'}
        if not user['is_active']:
            return {'success': False, 'error': 'Account is deactivated'}
        if not verify_password(password, user['salt'], user['hashed']):
            return {'success': False, 'error': 'Invalid username or password'}
        token = self.sessions.create_session(username)
        return {'success': True, 'token': token, 'message': f"Welcome, {username}!"}

    def logout(self, token: str) -> dict:
        if self.sessions.delete_session(token):
            return {'success': True, 'message': 'Logged out successfully'}
        return {'success': False, 'error': 'Invalid session token'}

    def get_current_user(self, token: str) -> dict | None:
        username = self.sessions.validate_session(token)
        if not username:
            return None
        return self.users.get_user(username)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    auth = AuthService()

    # Test 1 - Register
    result = auth.register("alice", "securepass123", "alice@example.com")
    assert result['success'], f"Test 1 failed: {result}"
    print("Test 1 passed - User registered successfully")

    # Test 2 - Duplicate register
    result = auth.register("alice", "anotherpass", "alice2@example.com")
    assert not result['success']
    print("Test 2 passed - Duplicate username rejected")

    # Test 3 - Login success
    result = auth.login("alice", "securepass123")
    assert result['success'], f"Test 3 failed: {result}"
    token = result['token']
    print("Test 3 passed - Login successful")

    # Test 4 - Wrong password
    result = auth.login("alice", "wrongpassword")
    assert not result['success']
    print("Test 4 passed - Wrong password rejected")

    # Test 5 - Session validation
    user = auth.get_current_user(token)
    assert user is not None and user['username'] == 'alice'
    print("Test 5 passed - Session valid")

    # Test 6 - Logout
    result = auth.logout(token)
    assert result['success']
    user = auth.get_current_user(token)
    assert user is None
    print("Test 6 passed - Logout and session invalidation works")

    # Test 7 - Validation errors
    result = auth.register("ab", "short", "notemail")
    assert not result['success']
    print("Test 7 passed - Validation errors caught correctly")

    print("\nAll tests passed for auth.py ✓")
