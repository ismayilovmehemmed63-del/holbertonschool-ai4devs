# Bug Reports - prompting_debug_assistant

---

## Bug Report - bug1.py
- **File**: bug1.py
- **Summary**: Syntax error and missing input validation for empty list.
- **Root Cause**: The function definition `def calculate_average(numbers)` was missing a colon (`:`). Additionally, there was no guard clause to handle empty lists, which would cause a `ZeroDivisionError`.
- **Resolution**: Added the missing colon to the function header. Added an `if len(numbers) == 0` check to return 0 for empty lists. Fix was AI-suggested, no manual edits needed.
- **Lesson Learned**: Always validate input before performing operations. Python syntax errors can be subtle and break execution entirely.

---

## Bug Report - bug2.js
- **File**: bug2.js
- **Summary**: Missing `await` keyword caused async function to return a pending Promise.
- **Root Cause**: The `fetchUserData()` call inside the `async` function was not preceded by `await`, so the variable `user` held an unresolved Promise object instead of the actual data.
- **Resolution**: Added `await` before `fetchUserData()`. Fix was AI-suggested, no manual edits needed.
- **Lesson Learned**: Always use `await` when calling Promise-based functions inside `async` functions, otherwise properties will return `undefined`.

---

## Bug Report - bug3.cpp
- **File**: bug3.cpp
- **Summary**: Off-by-one error in loop condition caused out-of-bounds memory access.
- **Root Cause**: The loop condition `i <= n` allowed the index to reach 5 in a 5-element array (valid indices: 0-4), causing a segmentation fault.
- **Resolution**: Changed `i <= n` to `i < n`. Fix was AI-suggested, no manual edits needed.
- **Lesson Learned**: In C++, array bounds are strictly 0 to n-1. Always use `<` instead of `<=` when iterating over arrays.

---

## Bug Report - bug4.py
- **File**: bug4.py
- **Summary**: Off-by-one error in range caused incorrect factorial result.
- **Root Cause**: `range(1, n)` excludes the value `n` in Python, so the last multiplication step was skipped. For input 5, the result was 24 instead of 120.
- **Resolution**: Changed `range(1, n)` to `range(1, n + 1)`. Fix was AI-suggested, no manual edits needed.
- **Lesson Learned**: Python's `range()` is exclusive of the stop value. Always use `n + 1` when the endpoint must be included.
