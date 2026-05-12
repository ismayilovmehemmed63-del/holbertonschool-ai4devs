# AI Review Log

**File Reviewed:** `auth.py`
**Feature:** User Authentication (register, login, logout, session management)
**AI Tools Used:** Claude (Anthropic), GitHub Copilot
**Date:** 2026-05-13

---

## Inline Comments

### 🔒 Security Persona

- **(line 12) `hash_password()`** — PBKDF2 iteration count of 100,000 is acceptable today but should be a named constant `PBKDF2_ITERATIONS = 100_000` so it can be updated without changing function logic.
- **(line 22) `verify_password()`** — Correct use of `hmac.compare_digest()` prevents timing attacks. Add a docstring explaining why `==` must never be used here.
- **(line 78) `create_session()`** — Replace `os.urandom(32).hex()` with `secrets.token_hex(32)` — the stdlib-recommended API for cryptographic tokens since Python 3.6.
- **(line 110) `AuthService.register()`** — Email validation only checks for presence of `@`. Use `re` module to reject malformed addresses like `a@` or `@b.com`.
- **(line 118) `AuthService.register()`** — Password policy only enforces minimum length. Require at least one digit and one special character to meet standard security policies.
- **(line 130) `AuthService.login()`** — No brute-force protection. Add a failed-attempt counter per username and lock the account for 5 minutes after 5 consecutive failures.
- **(line 145) `AuthService.get_current_user()`** — Returns raw user dict containing `salt` and `hashed` password. Strip sensitive fields before returning data to callers.

### ⚡ Performance Persona

- **(line 67) `SessionManager.SESSION_TTL`** — Sessions expire after 1 hour but are only removed lazily on access. Under high concurrency, stale sessions accumulate and waste memory.
- **(line 88) `validate_session()`** — Expired sessions deleted one at a time. Add a `cleanup_expired_sessions()` batch method and call it every N logins to keep memory bounded.
- **(line 35) `UserStore._users`** — Plain `dict` lookup is O(1) but offers no indexing by email. If email-based lookups are needed later, a secondary index dict `_emails` should be maintained in parallel.

### 🛠️ Maintainability Persona

- **(line 35) `UserStore._users`** — In-memory store loses all data on restart. Add a comment clearly warning this is not production-ready without a persistent backend.
- **(line 48) `add_user()`** — No duplicate email check. Two accounts with the same email make password-reset flows impossible. Add email uniqueness validation.
- **(line 95) `AuthService.__init__()`** — `UserStore` and `SessionManager` are instantiated internally, making unit testing difficult. Inject them as constructor parameters to enable mocking.

---

## Global Feedback

### 🔒 Security

- **No rate limiting:** The `login()` method has no lockout after repeated failures. A brute-force attack can cycle through passwords indefinitely. Implement exponential backoff or account lockout after 5 failed attempts.
- **Sensitive data exposure:** `get_current_user()` leaks password hash and salt to callers. Add a `sanitize_user()` helper returning only `username`, `email`, `created_at`, and `is_active`.
- **Weak email validation:** Regex or a dedicated library (e.g., `email-validator`) should replace the single `@` check to prevent invalid registrations.

### ⚡ Performance

- **Session memory leak:** Expired sessions accumulate indefinitely. Introduce a `cleanup_expired_sessions()` method triggered periodically (e.g., every 100 logins) or use a TTL-aware cache like `cachetools.TTLCache`.
- **Thread safety:** `UserStore._users` and `SessionManager._sessions` are plain dicts. Concurrent writes in a multi-threaded server risk data corruption. Protect mutations with `threading.Lock()`.

### 🛠️ Maintainability

- **Single Responsibility violation:** `AuthService` combines business logic and data access. Refactor by extracting a `UserRepository` class for persistence, keeping `AuthService` focused on auth logic only.
- **No logging:** Auth events (login success, login failure, logout, registration) must be logged for auditing. Integrate Python `logging` module with appropriate levels (`INFO`, `WARNING`).
- **Missing module docstring:** The file has no top-level docstring. Add one per PEP 257 describing the module's purpose, public classes, and a usage example.
- **Hard-coded dependencies:** Constructor should accept `user_store` and `session_manager` as optional parameters with defaults, enabling dependency injection for testing.
