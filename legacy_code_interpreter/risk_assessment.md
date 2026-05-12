# Risk Assessment – Legacy Student Management System

## Risk 1 – SQL Injection Vulnerabilities
- **Severity**: High
- **Notes**: User input is concatenated directly into SQL queries in authenticate_user() and save_student_data(). Attackers can manipulate queries to access or destroy all database records.

## Risk 2 – Broken Password Hashing
- **Severity**: High
- **Notes**: All passwords are stored as unsalted MD5 hashes. MD5 is cryptographically broken and easily reversible using publicly available rainbow tables, exposing all user credentials.

## Risk 3 – Hardcoded Database Credentials
- **Severity**: High
- **Notes**: Database username and password are written directly in source files instead of environment variables. Any developer or attacker with source access can compromise the entire database.

## Risk 4 – Zero Test Coverage
- **Severity**: Medium
- **Notes**: No unit tests, integration tests, or automated tests exist anywhere in the codebase. Any code change risks introducing undetected regressions in critical business logic.

## Risk 5 – End-of-Life Dependencies
- **Severity**: Medium
- **Notes**: The system runs on PHP 5.3 and MySQL 5.1, both of which reached end-of-life and no longer receive security patches. Known vulnerabilities in these versions remain permanently unpatched.

## Risk 6 – No Input Validation
- **Severity**: High
- **Notes**: Raw form data is inserted into the database without any validation or sanitization. This allows malformed, malicious, or corrupted data to be permanently stored in the system.

## Risk 7 – No Error Handling or Logging
- **Severity**: Medium
- **Notes**: Database failures and application errors crash silently with no logs generated. This makes debugging production issues extremely difficult and leaves no audit trail for incidents.
