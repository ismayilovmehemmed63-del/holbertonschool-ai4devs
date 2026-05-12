# Fix Validation - Smart Bug Bounty

## bug1.py
- Original Issue: get_top_students() sorted in ascending order, returning lowest scoring students instead of top performers.
- Fix Applied: Added reverse=True to sorted() call to sort in descending order.
- Test Results: All 3 test cases passed. Top 2 students correctly returned as Alice (92) and Carol (88).

## bug2.js
- Original Issue: Loop used i <= items.length causing off-by-one error and TypeError on undefined index.
- Fix Applied: Changed <= to < in loop condition. Fixed == to === in findUser(). Added return null for not-found case.
- Test Results: calculateTotal returns correct sum 4.25. findUser returns correct user or null. All tests passed.

## bug3.cpp
- Original Issue: Loop used i <= arr.size() causing out-of-bounds access. Return statement before cout made output unreachable.
- Fix Applied: Changed i <= arr.size() to i < arr.size(). Moved cout before return statement.
- Test Results: findMax correctly returns 9 for input array. greet prints output correctly. All tests passed.

## bug4.c
- Original Issue: Buffer overflow with strcpy() and division by zero in divide().
- Fix Applied: Replaced strcpy with strncpy with size limit and null terminator. Added zero-check before division.
- Test Results: Short strings copied safely. Division by zero returns -1 with error message. All tests passed.

## bug5.py
- Original Issue: File opened without context manager. parse_config() crashed on lines without equals sign. Password hardcoded.
- Fix Applied: Used with statement for file reading with try-except. Added guard for lines without equals sign. Used os.environ.get() for password.
- Test Results: Non-existent file returns None safely. Invalid config lines skipped. All 3 assertions passed.
