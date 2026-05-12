# Risk Assessment – Legacy Student Management System

| Risk | Severity | Notes |
|------|----------|-------|
| SQL Injection vulnerabilities | High | User input concatenated directly into SQL queries in multiple functions including authenticate_user() and save_student_data() |
| Broken password hashing (MD5) | High | All passwords stored as unsalted MD5 hashes which are easily reversible using rainbow tables |
| Hardcoded database credentials | High | Database username and password written directly in source files instead of environment variables |
| No input validation or sanitization | High | Raw form data inserted into database without any checks, allowing malformed or malicious data storage |
| XSS vulnerabilities in output | High | HTML output built by concatenating unescaped user data, enabling cross-site scripting attacks |
| Zero test coverage | Medium | No unit tests, integration tests, or automated tests of any kind exist across the entire codebase |
| Session fixation vulnerability | Medium | Session IDs not regenerated after login, allowing attackers to hijack authenticated sessions |
| No CSRF protection | Medium | No CSRF tokens on any form submissions, making state-changing requests vulnerable to forgery |
| Sensitive data stored unencrypted | Medium | Personal student information stored in plain text in the database with no encryption at rest |
| End-of-life dependencies | Medium | PHP 5.3 and MySQL 5.1 are both end-of-life with no security patches available |
| No error handling or logging | Medium | Database failures and application errors crash silently with no logs for debugging or auditing |
| Tight coupling between modules | Medium | Business logic, data access, and presentation mixed together making refactoring extremely difficult |
| No audit trail for data changes | Low | No record of who modified student data or when changes were made |
| Inconsistent coding standards | Low | Mixed procedural and OOP styles with inconsistent naming conventions across files |
| No caching mechanism | Low | Repeated database queries for the same data with no caching layer, reducing performance under load |
