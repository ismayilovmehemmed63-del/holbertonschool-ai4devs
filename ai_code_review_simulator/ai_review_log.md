# AI Review Log

## Overview

| Field | Detail |
|-------|--------|
| File Reviewed | `auth.py` |
| Feature | User Authentication (register, login, logout, session management) |
| AI Tools Used | Claude (Anthropic), GitHub Copilot |
| Review Date | 2026-05-13 |
| Inline Comments | 13 |
| Global Suggestions | 12 |
| Personas Applied | Security, Performance, Maintainability |

---

## Inline Comments

### Persona: Security

- **(line 12)** `hash_password()` — The PBKDF2 iteration count `100000` is hardcoded. Extract it as `PBKDF2_ITERATIONS = 100_000` at module level. OWASP 2023 recommends at least 600,000 iterations for SHA-256; making it a constant allows easy updates without touching function logic.

- **(line 22)** `verify_password()` — `hmac.compare_digest()` is correctly used to prevent timing attacks. Add an inline comment explaining why `==` must never replace it: `# compare_digest prevents timing oracle attacks`.

- **(line 78)** `create_session()` — Token generated via `os.urandom(32).hex()`. Replace with `secrets.token_hex(32)` — the stdlib-recommended API for cryptographic tokens since Python 3.6. It signals security intent clearly to auditors.

- **(line 110)** `AuthService.register()` — Email validation uses only `'@' not in email`. This accepts `a@`, `@b`, and `@@`. Apply `re.match(r'^[^@]+@[^@]+\.[^@]+$', email)` at minimum, or use the `email-validator` package for RFC 5322 compliance.

- **(line 118)** `AuthService.register()` — Password policy only checks minimum length. Enforce at least one uppercase letter, one digit, and one special character using `re.search()` patterns. Document the policy in the docstring.

- **(line 130)** `AuthService.login()` — No brute-force protection exists. Add `_failed_attempts: dict[str, int]` and `_lockout_until: dict[str, float]`. Lock accounts for 300 seconds after 5 consecutive failures. Log each failure event with `logger.warning()`.

- **(line 145)** `AuthService.get_current_user()` — Returns raw user dict including `salt` and `hashed` fields. Add `_sanitize_user(user)` that returns only `username`, `email`, `created_at`, `is_active`. Apply it to every method that returns user data.

### Persona: Performance

- **(line 67)** `SessionManager.SESSION_TTL` — Magic number `3600` should be `SESSION_TTL_SECONDS = 3600  # 1 hour expiry`. Consider reading from `os.getenv('SESSION_TTL', 3600)` for environment-specific configuration.

- **(line 88)** `validate_session()` — Expired sessions are deleted lazily on access only. In a long-running server, stale sessions accumulate unboundedly. Add `cleanup_expired_sessions()` and call it every 100 logins via an internal counter.

- **(line 35)** `UserStore._users` — Dict lookup by username is O(1). However, email-based lookups (needed for password reset) require O(n) linear scan. Maintain a parallel `_emails: dict[str, str]` mapping `email → username` for O(1) email lookups.

### Persona: Maintainability

- **(line 35)** `UserStore` class — No persistence warning is present. Add a docstring: `WARNING: In-memory store only. Data is lost on restart. Replace with a database-backed repository for production.`

- **(line 95)** `AuthService.__init__()` — `UserStore` and `SessionManager` are instantiated internally, preventing dependency injection and unit test mocking. Change to: `def __init__(self, user_store=None, session_manager=None)` with internal defaults when `None`.

- **(line 48)** `add_user()` — No email uniqueness check. Two accounts can share the same email, breaking password-reset and account-recovery flows. Validate email uniqueness in both `UserStore.add_user()` and `AuthService.register()`.

---

## Global Feedback

### Persona: Security

- **Audit logging missing:** Every auth event (login success, login failure, logout, registration, lockout) must be logged for security auditing and incident response. Use Python `logging` module. Emit `logger.info()` for successes and `logger.warning()` for failures. Never log passwords, salts, or tokens.

- **No rate limiting on registration:** The `register()` method has no throttling. An attacker can create thousands of accounts programmatically. Add per-IP or per-email rate limiting with exponential backoff.

- **Account lockout policy undefined:** After repeated failures, accounts remain unlocked indefinitely. Implement tiered lockout: 5 failures → 5-minute lock, 10 failures → 1-hour lock, 20 failures → permanent lock requiring admin intervention.

- **Sensitive data exposure:** `get_current_user()` leaks `salt` and `hashed` to all callers. Apply `_sanitize_user()` consistently. Document which fields are public vs. internal in the class docstring.

### Persona: Performance

- **Unbounded session memory growth:** Expired sessions are never proactively removed. Introduce `cleanup_expired_sessions()` on `SessionManager`. Trigger it every 100 `create_session()` calls using an internal `_login_count` counter. Alternatively, replace `_sessions` dict with `cachetools.TTLCache` for automatic expiry.

- **Thread safety not guaranteed:** `UserStore._users` and `SessionManager._sessions` are plain dicts. Concurrent writes from multiple threads cause race conditions and data corruption. Wrap all mutations in `threading.Lock()`. Add `_lock = threading.Lock()` to both classes.

- **No database migration path:** When replacing the in-memory store with a real database, connection pooling and query optimization will be critical. Add `TODO` comments at `UserStore` recommending SQLAlchemy with `pool_size` and `max_overflow` configuration.

### Persona: Maintainability

- **Single Responsibility Principle violated:** `AuthService` combines input validation, business logic, and data access. Extract `UserRepository` for all CRUD operations. `AuthService` should depend on an abstract `BaseUserRepository` interface, enabling swappable backends (SQLite, PostgreSQL, Redis).

- **No structured logging:** Add structured log entries with context fields. Example: `logger.info("LOGIN_SUCCESS", extra={"username": username})`. This enables log aggregation tools (ELK Stack, Datadog) to parse and alert on anomalies.

- **Missing TypedDict definitions:** Methods return plain `dict` without schema documentation. Define `UserRecord(TypedDict)` and `AuthResult(TypedDict)` to make return types explicit, IDE-friendly, and self-documenting.

- **No configuration management:** `SESSION_TTL`, `PBKDF2_ITERATIONS`, and password length minimums are scattered constants. Consolidate into an `AuthConfig` dataclass with `os.getenv()` overrides for environment-specific deployment.

- **Test coverage gaps:** Current tests cover only happy path and basic negatives. Add edge-case tests: empty string inputs, Unicode passwords, concurrent login attempts, session reuse after logout, and SQL injection patterns in username field.

---

## Review Checklist

| Category | Item | Status |
|----------|------|--------|
| Security | Password hashing with salt | ✅ Implemented |
| Security | Timing-safe comparison | ✅ Implemented |
| Security | Brute-force protection | ❌ Missing |
| Security | Email validation | ⚠️ Weak |
| Security | Sensitive data sanitization | ❌ Missing |
| Security | Audit logging | ❌ Missing |
| Performance | Session cleanup | ❌ Missing |
| Performance | Thread safety | ❌ Missing |
| Performance | Email index for O(1) lookup | ❌ Missing |
| Maintainability | Dependency injection | ❌ Missing |
| Maintainability | Persistence warning | ❌ Missing |
| Maintainability | TypedDict return types | ❌ Missing |
| Maintainability | Configuration management | ❌ Missing |
