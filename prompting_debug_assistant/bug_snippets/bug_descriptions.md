# Project: Prompting Debug Assistant - Bug Descriptions

## Bug 1
**File Name:** bug1.py
**Intended Behavior:** The function `calculate_average` should return the mean of a list and handle empty lists by returning 0. The `get_last_n_elements` function should return the last `n` elements safely using valid zero-based indices.
**Issue Type:** ZeroDivisionError and IndexError (Out of Bounds).
**Solution Suggestion:** Add an `if not numbers: return 0` check in the average function and fix the loop range in the slicing function to `len(items)`.

## Bug 2
**File Name:** bug2.js
**Intended Behavior:** The script should asynchronously fetch user data and ensure the `user` variable is populated before the dashboard attempts to access its properties (name/role).
**Issue Type:** Asynchronous Logic Error (Race Condition).
**Solution Suggestion:** Implement a Promise or use `async/await` to wait for the `setTimeout` callback to complete before calling `displayDashboard`.

## Bug 3
**File Name:** bug3.cpp
**Intended Behavior:** The program should allocate an array that remains valid in memory during its usage in `main`, and the iteration should stay within the array's defined size.
**Issue Type:** Memory Safety (Dangling Pointer) and Buffer Overflow.
**Solution Suggestion:** Use dynamic memory allocation (`new`) for the array or pass the array by reference, and fix the loop condition from `i <= n` to `i < n`.

## Bug 4
**File Name:** bug4.py
**Intended Behavior:** The script should take numerical input, convert it to an integer, and calculate the factorial recursively with a base case that handles negative numbers safely.
**Issue Type:** Logic Error (Infinite Recursion) and TypeError.
**Solution Suggestion:** Convert `user_val` using `int()`, and add a check to ensure `n` is non-negative before starting the recursion.
