# AI Review Log

**File Reviewed:** `auth.py`
**Feature:** User Authentication (register, login, logout, session management)
**AI Tools Used:** Claude (Anthropic), GitHub Copilot
**Date:** 2026-05-13

---

## Inline Comments

- **(line 12) `hash_password()`** — PBKDF2 iteration count of 100,000 is acceptable today but should be configurable via a constant (e.g., `PBKDF2_ITERATIONS = 100_000`) so it can be increased without touching function logic.

- **(line 22) `verify_password()`** — Good use of `hmac.compare_digest()` to prevent timing attacks. Consider adding a docstring note explaining *why* this is used instead of `==`.

- **(line 35) `UserStore._users`** — Using a plain `dict` means data is lost on restart. Add a comment warning that this is in-memory only and not suitable for production without a persistent backend.

- **(line 48) `add_user()`** — No check for duplicate email addresses. Two users could register with the same email, making password-reset flows impossible later.

- **(line 67) `SessionManager.SESSION_TTL`** — Magic number `3600` should be a named constant with a comment explaining the business rule (1-hour session expiry).

- **(line 78) `create_session()`** — Session token is generated with `os.urandom(32).hex()` which is cryptographically secure. Consider using `secrets.token_hex(32)` instead — it is the stdlib-recommended API for security tokens since Python 3.6.

- **(line 88) `validate_session()`** — Expired sessions are deleted lazily (only when accessed). Under high load, stale sessions accumulate in memory. Add a periodic cleanup method or use TTL-aware data structures.

- **(line 110) `AuthService.register()`** — Email validation only checks for `@`. Use `re` module or a dedicated validator to catch obviously malformed addresses like `a@` or `@b`.

- **(line 118) `AuthService.register()`** — Password strength check only enforces minimum length. Consider checking for at least one digit and one special character to meet common security policies.

- **(line 130) `AuthService.login()`** — No rate limiting or account lockout after repeated failed attempts. A brute-force attack could cycle through passwords indefinitely.

- **(line 145) `AuthService.get_current_user()`** — Returns the full user dict including `salt` and `hashed` fields. Sensitive fields should be stripped before returning user data to callers.

---

## Global Feedback

- **Security — No rate limiting:** The login function has no lockout mechanism. Recommend adding a failed-attempt counter per username with a cooldown (e.g., lock for 5 minutes after 5 failures).

- **Security — Sensitive data exposure:** `get_current_user()` returns the raw user record including password hash and salt. Create a `sanitize_user()` helper that returns only safe fields (`username`, `email`, `created_at`, `is_active`).

- **Maintainability — Single Responsibility:** `AuthService` handles both business logic and data access. Consider separating into a `UserRepository` for persistence and an `AuthService` for logic, following the Repository pattern.

- **Maintainability — No logging:** Production auth systems must log login attempts, failures, and logouts (without logging passwords). Add a `logging` module integration with appropriate log levels.

- **Performance — Session cleanup:** Expired sessions are never proactively removed. Add a `cleanup_expired_sessions()` method and call it periodically (e.g., on every 100th login) to prevent unbounded memory growth.

- **Testability — Hard-coded dependencies:** `AuthService` instantiates `UserStore` and `SessionManager` internally. Inject them as constructor parameters to allow mocking in unit tests.

- **Robustness — Thread safety:** `UserStore._users` and `SessionManager._sessions` are plain dicts. In a multi-threaded server, concurrent writes could corrupt state. Use `threading.Lock()` or switch to thread-safe structures.

- **Documentation — Missing module docstring:** The file lacks a top-level docstring describing the module's purpose, public API, and usage example. Add one following PEP 257 conventions.
