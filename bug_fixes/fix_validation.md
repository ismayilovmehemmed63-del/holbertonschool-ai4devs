# Fix Validation – Smart Bug Bounty

## bug1.py
- **Original Issue**: get_top_students() sorted in ascending order, returning lowest scoring students instead of top performers.
- **Fix Applied**: Added reverse=True to sorted() call to sort in descending order.
- **Test Results**: All 3 test cases passed. Top 2 students correctly returned as Alice (92) and Carol (88).

## bug2.js
- **Original Issue**: Loop used i <= items.length causing off-by-one error and TypeError on undefined index.
- **Fix Applied**: Changed <= to < in loop condition. Also fixed == to === for strict equality in findUser(). Added return null for not-found case.
- **Test Results**: calculateTotal returns correct sum 4.25. findUser returns correct user or null.

## bug3.java
- **Original Issue**: deposit() used =+ instead of +=, assigning instead of adding to balance.
- **Fix Applied**: Changed balance =+ amount to balance += amount.
- **Test Results**: Deposit of 500 to account with 1000 correctly results in 1500. Withdrawal of 200 correctly results in 1300. Overdraft correctly prevented.

## bug4.c
- **Original Issue**: Buffer overflow with strcpy() and division by zero in divide().
- **Fix Applied**: Replaced strcpy with strncpy with size limit and null terminator. Added zero-check before division.
- **Test Results**: Short strings copied safely. Division by zero returns -1 with error message. Normal division works correctly.

## bug5.py
- **Original Issue**: File opened without context manager. parse_config() crashed on lines without equals sign. Password hardcoded in connection string.
- **Fix Applied**: Used with statement for file reading with try-except. Added if '=' not in line: continue guard. Replaced hardcoded password with os.environ.get('DB_PASSWORD').
- **Test Results**: Non-existent file returns None safely. Invalid config lines skipped. All 3 test assertions passed.
