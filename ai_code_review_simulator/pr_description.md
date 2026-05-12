# Pull Request: Add User Authentication Feature

## Summary
Implements a complete user authentication system with registration, login, logout,
password hashing, and session management. All logic is encapsulated in `auth.py`.

## Changes
- Added `hash_password()` — PBKDF2-HMAC-SHA256 with random salt
- Added `verify_password()` — constant-time comparison to prevent timing attacks
- Added `UserStore` class — in-memory user database with activation support
- Added `SessionManager` class — token-based sessions with 1-hour TTL and expiry
- Added `AuthService` class — main service combining registration, login, logout
- Added 7 unit tests covering success and failure scenarios

## Context
~160 LOC. Implements secure authentication best practices:
- Passwords never stored in plaintext
- Salt generated with os.urandom(32)
- Session tokens generated with os.urandom(32)
- Constant-time password comparison with hmac.compare_digest
- Input validation on all fields

## Test Results
All 7 tests passed:
- User registration
- Duplicate username rejection
- Successful login
- Wrong password rejection
- Session validation
- Logout and session invalidation
- Input validation errors
