# Project: Prompting Debug Assistant - Bug Descriptions

## Bug 1 - bug1.py
**Intended Behavior:**
The `calculate_average` function is designed to safely calculate the mean of a list of numbers. It should include a check for empty lists to return 0 or a message, preventing a crash. The `get_last_n_elements` function is intended to return a sub-list of the last `n` items without exceeding the valid index range of the list.

**Issue Type:** ZeroDivisionError and Index Out of Range.
**Detailed Notes:**
* **ZeroDivisionError:** The script crashes with a ZeroDivisionError when an empty list is passed because `len(numbers)` becomes zero.
* **Off-by-one Error:** The loop `range(start_index, len(items) + 1)` attempts to access `items[len(items)]`, which is out of bounds for a zero-indexed list.

---

## Bug 2 - bug2.js
**Intended Behavior:**
This script aims to simulate a database fetch. The `fetchUserData` function should ideally use a Promise or callback to ensure that the `user` data is fully loaded before `displayDashboard` attempts to access the user's name or role.

**Issue Type:** Asynchronous Execution / Null Pointer Reference.
**Detailed Notes:**
* **Async Mismanagement:** `setTimeout` does not block execution. The function returns `null` immediately before the 2-second timer finishes.
* **Null Reference:** `userData.name` fails because `userData` is still `null` at the moment of execution.

---

## Bug 3 - bug3.cpp
**Intended Behavior:**
The program is intended to allocate memory for an integer array, fill it with data, and safely print those values in the `main` function. It should manage memory lifecycles so that pointers remain valid during traversal.

**Issue Type:** Memory Safety / Dangling Pointer / Segmentation Fault.
**Detailed Notes:**
* **Dangling Pointer:** Returning the address of a local array `int arr[size]` is dangerous because that memory is freed once `createArray` returns.
* **Out of Bounds:** The loop condition `i <= n` attempts to access the 6th element of a 5-element array, leading to memory corruption.

---

## Bug 4 - bug4.py
**Intended Behavior:**
The script is intended to take a user's numerical input, convert it to an integer, and calculate its factorial using recursion. It should handle non-integer strings and negative numbers without causing a crash or infinite recursion.

**Issue Type:** Recursion Error / Type Mismatch.
**Detailed Notes:**
* **Infinite Recursion:** No base case for negative numbers exists; `factorial(-1)` will call `factorial(-2)` forever until the stack overflows.
* **Type Error:** `input()` returns a string. The code fails when it tries to subtract 1 from a string (`user_val - 1`).
