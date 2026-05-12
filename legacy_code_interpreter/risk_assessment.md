# Risk Assessment – Legacy Student Management System

## Risk 1 – SQL Injection Vulnerabilities
- **Severity**: High
- **Notes**: User input is concatenated directly into SQL queries without sanitization. Attackers can manipulate queries to bypass authentication, extract all database records, or permanently delete data. This affects every database operation in the system.

## Risk 2 – Broken Password Hashing with MD5
- **Severity**: High
- **Notes**: All user passwords are stored as unsalted MD5 hashes. MD5 is cryptographically broken and rainbow table attacks can reverse these hashes in seconds. A single database breach exposes every user password immediately.

## Risk 3 – Hardcoded Database Credentials in Source Code
- **Severity**: High
- **Notes**: Database hostname, username, and password are written directly in PHP source files with no use of environment variables or secrets management. Any person with repository access can gain full database control.

## Risk 4 – Zero Automated Test Coverage
- **Severity**: Medium
- **Notes**: No unit tests, integration tests, or regression tests exist anywhere in the codebase. Every deployment carries an unknown risk of breaking existing functionality with no safety net to catch errors before they reach production.

## Risk 5 – End-of-Life Runtime Dependencies
- **Severity**: Medium
- **Notes**: The system depends on PHP 5.3 (EOL 2014) and MySQL 5.1 (EOL 2013). These versions no longer receive security patches, meaning all known and future vulnerabilities in these runtimes remain permanently unaddressed in this system.
