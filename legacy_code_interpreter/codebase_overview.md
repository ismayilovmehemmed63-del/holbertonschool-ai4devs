# Codebase Overview – Legacy Student Management System

## Age
First release in 2008, last major update in 2014.
The codebase has not received significant maintenance since 2016.

## Size
- Approximately 32,000 lines of code (LOC)
- Written primarily in PHP 5.3 with some embedded JavaScript
- 180+ files across 12 modules

## Main Dependencies
- PHP 5.3 (end-of-life since 2014)
- MySQL 5.1 (end-of-life since 2013)
- jQuery 1.6 (heavily outdated)
- Deprecated MD5-based authentication library
- Custom session management without CSRF protection
- No package manager (no Composer or npm)

## Known Issues and Pain Points
- No automated tests of any kind (0% test coverage)
- Mixed procedural and object-oriented programming styles
- SQL queries built with string concatenation (SQL injection risk)
- Passwords stored as plain MD5 hashes without salting
- No input sanitization or output escaping (XSS vulnerabilities)
- High coupling between modules — changes in one area break others
- No error logging or monitoring system
- Database credentials hardcoded in multiple source files
- No version control history prior to 2012
- Inconsistent naming conventions across files and functions
- Large functions exceeding 300 lines with no separation of concerns
- No API layer — frontend and backend logic mixed in same files
