# AI Review Log

**File Reviewed:** `auth.py`
**Feature:** User Authentication
**AI Tools Used:** Claude (Anthropic), GitHub Copilot
**Date:** 2026-05-13

---

## Inline Comments

### Persona: Security

- **(line 12) hash_password() - Hardcoded iteration count:**
  The PBKDF2 iteration count 100000 is hardcoded directly in the function body. Extract it as a module-level constant `PBKDF2_ITERATIONS = 100_000` so future security upgrades require only a single change.

- **(line 22) verify_password() - Timing-safe comparison:**
  The function correctly uses `hmac.compare_digest()` to prevent timing-based attacks. Add an inline comment explaining that `==` must never replace this, so future maintainers do not accidentally introduce a vulnerability.

- **(line 78) create_session() - Weak token API:**
  The session token uses `os.urandom(32).hex()` which is secure but not the recommended API. Replace it with `secrets.token_hex(32)`, which is the stdlib standard for cryptographic tokens since Python 3.6 and signals intent clearly to security auditors.

- **(line 110) register() - Weak email validation:**
  Email validation only checks for the presence of `@`, which accepts invalid addresses like `a@` or `@b`. Apply `re.match(r'^[^@]+@[^@]+\.[^@]+$', email)` at minimum, or use the `email-validator` package for full RFC 5322 compliance.

- **(line 130) login() - No brute-force protection:**
  The login method allows unlimited password attempts with no lockout mechanism. Add a `_failed_attempts` counter per username and lock the account for 300 seconds after 5 consecutive failures, logging each failed attempt with `logger.warning()`.

- **(line 145) get_current_user() - Sensitive data leakage:**
  This method returns the raw user dictionary including `salt` and `hashed` password fields to all callers. Add a `_sanitize_user()` private method that returns only `username`, `email`, `created_at`, and `is_active`, and apply it consistently.

### Persona: Performance

- **(line 67) SESSION_TTL - Magic number:**
  The session expiry value `3600` is a magic number with no explanation in the code. Define `SESSION_TTL_SECONDS = 3600  # 1 hour` as a named constant and consider reading it from `os.getenv('SESSION_TTL', 3600)` for environment-specific configuration.

- **(line 88) validate_session() - Lazy expiry only:**
  Expired sessions are only removed when they are individually accessed, meaning stale sessions accumulate in memory indefinitely in a long-running server. Add a `cleanup_expired_sessions()` method that removes all expired entries and call it every 100 logins via an internal counter.

- **(line 35) UserStore._users - No email index:**
  User lookup is by username only, which is O(1). However, email-based lookups needed for password-reset flows require an O(n) linear scan of all users. Maintain a parallel `_emails: dict[str, str]` mapping email to username for O(1) email lookups.

### Persona: Maintainability

- **(line 35) UserStore - No persistence warning:**
  The in-memory store loses all user data when the process restarts, but there is no warning in the code. Add a class-level docstring stating clearly: `WARNING: In-memory store only. Data is lost on restart. Replace with a database-backed repository for production.`

- **(line 95) AuthService.__init__() - Hard-coded dependencies:**
  `UserStore` and `SessionManager` are instantiated inside `__init__`, making it impossible to inject mocks during unit testing. Change the signature to `def __init__(self, user_store=None, session_manager=None)` and create default instances only when `None` is passed.

- **(line 48) add_user() - No email uniqueness check:**
  Two users can register with the same email address because no uniqueness constraint exists. Add an email uniqueness check in both `UserStore.add_user()` and `AuthService.register()` to prevent broken password-reset and account-recovery flows.

- **(line 118) register() - Weak password policy:**
  The password check only enforces a minimum length of 8 characters, which is insufficient for a secure system. Require at least one uppercase letter, one digit, and one special character using `re.search()` patterns, and document the policy in the method docstring.

---

## Global Feedback

### Persona: Security

- **Audit logging is completely missing from the module.**
  Every authentication event including login success, login failure, logout, registration, and account lockout must be logged for security auditing and incident response. Integrate Python `logging` module and emit `logger.info()` for successes and `logger.warning()` for failures, never logging passwords, salts, or tokens.

- **No rate limiting exists on the registration endpoint.**
  An attacker can create thousands of fake accounts with no throttling or cooldown. Implement per-IP or per-email rate limiting with exponential backoff to prevent automated account creation abuse.

- **Account lockout policy is completely undefined.**
  After any number of failed login attempts, the account remains accessible with no consequence. Implement a tiered lockout: 5 failures triggers a 5-minute lock, 10 failures triggers a 1-hour lock, and 20 failures triggers a permanent lock requiring admin reset.

### Persona: Performance

- **Expired sessions accumulate indefinitely causing memory growth.**
  The `SessionManager` has no proactive cleanup mechanism, so stale sessions remain in `_sessions` forever in a long-running server. Add `cleanup_expired_sessions()` and trigger it every 100 calls to `create_session()`, or replace `_sessions` with `cachetools.TTLCache` for automatic expiry.

- **Neither UserStore nor SessionManager is thread-safe.**
  Both classes use plain Python dicts which are not safe for concurrent writes from multiple threads in a web server context. Add `_lock = threading.Lock()` to both classes and wrap all mutation operations in `with self._lock:` blocks.

### Persona: Maintainability

- **AuthService violates the Single Responsibility Principle.**
  The class combines input validation, business logic, and data access in one place, making it hard to test and extend independently. Extract a `UserRepository` class for all CRUD operations and have `AuthService` depend on an abstract `BaseUserRepository` interface.

- **Structured logging is absent throughout the entire module.**
  Without log entries, diagnosing authentication failures or auditing suspicious activity in production is impossible. Add structured log statements with context fields such as `logger.info("LOGIN_SUCCESS", extra={"username": username})` for compatibility with ELK Stack or Datadog.

- **Return types are undocumented plain dicts throughout.**
  Methods return generic `dict` objects with no schema, making it unclear to callers what fields to expect. Define `UserRecord(TypedDict)` and `AuthResult(TypedDict)` classes to make return types explicit, self-documenting, and IDE-friendly.
