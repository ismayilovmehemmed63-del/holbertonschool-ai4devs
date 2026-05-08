# Bug Descriptions - AI Debugging Project

## Bug 1
**File Name:** bug1.py
**Intended Behavior:** The function `calculate_average` should return the mean of a list and return 0 if the list is empty. The function `get_last_n_elements` should return exactly the last `n` elements of a list using valid indices.
**Issue Type:** ZeroDivisionError and Index Out of Range.
**Detailed Notes:** The code lacks a check for empty input, leading to division by zero. Also, the loop boundary goes to `len(items) + 1`, causing an access beyond the list's capacity.

## Bug 2
**File Name:** bug2.js
**Intended Behavior:** The script should asynchronously fetch user data and wait for the response to be stored in the `user` variable before attempting to log properties like `name` or `role`.
**Issue Type:** Asynchronous Logic Error / Null Pointer Exception.
**Detailed Notes:** The `user` variable remains `null` when the function returns because `setTimeout` is non-blocking. Accessing `userData.name` results in a crash.

## Bug 3
**File Name:** bug3.cpp
**Intended Behavior:** The program should allocate an array in memory that persists long enough for the `main` function to read it, and it should iterate exactly `n` times to print the values.
**Issue Type:** Memory Management / Segmentation Fault.
**Detailed Notes:** Returning a pointer to a local stack-allocated array creates a dangling pointer. The loop condition `i <= n` results in an off-by-one error, accessing invalid memory.

## Bug 4
**File Name:** bug4.py
**Intended Behavior:** The script should accept a numerical input from the user, convert it to an integer type, and calculate the factorial using a recursive base case that prevents infinite loops with negative numbers.
**Issue Type:** Logic Error (Infinite Recursion) and Type Mismatch.
**Detailed Notes:** No validation for negative numbers leads to a stack overflow. The `input()` function returns a string, which causes mathematical operations to fail.
