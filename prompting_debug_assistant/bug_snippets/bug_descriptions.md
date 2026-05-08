# Project: Prompting Debug Assistant - Bug Descriptions

## Bug 1 - bug1.py
**Intended Behavior:**
The `calculate_average` function is intended to take a list of numbers and return their arithmetic mean. It should handle empty lists gracefully. The `get_last_n_elements` function is intended to safely return a slice of the last `n` items from a list using zero-based indexing.

**Issue Type:** ZeroDivisionError and Index Out of Range.
**Detailed Notes:**
* **ZeroDivisionError:** The code fails to check if the input list is empty before dividing by its length.
* **Off-by-one Error:** The loop range `range(start_index, len(items) + 1)` attempts to access an index that is out of bounds.

---

## Bug 2 - bug2.js
**Intended Behavior:**
The purpose of this script is to simulate an asynchronous data fetch. The `fetchUserData` function should ensure that the `user` object is fully populated before any dashboard display functions attempt to access its properties.

**Issue Type:** Asynchronous Execution / Null Pointer Reference.
**Detailed Notes:**
* **Async Mismanagement:** The function returns `null` immediately because `setTimeout` is non-blocking and does not pause execution.
* **Property Access on Null:** The code crashes when trying to read properties from a `null` object.

---

## Bug 3 - bug3.cpp
**Intended Behavior:**
This C++ program is intended to allocate memory for an integer array, initialize it, and print the values. It aims to demonstrate safe memory management and array traversal.

**Issue Type:** Memory Safety / Dangling Pointer / Segmentation Fault.
**Detailed Notes:**
* **Dangling Pointer:** The function returns the address of a local array that is destroyed after the function returns.
* **Buffer Overflow:** The loop condition `i <= n` causes an access to an invalid memory index.

---

## Bug 4 - bug4.py
**Intended Behavior:**
The script is intended to calculate the factorial of a positive integer provided by the user. It should convert the string input to an integer and handle the recursive calculation safely.

**Issue Type:** Recursion Error / Type Mismatch.
**Detailed Notes:**
* **Infinite Recursion:** No check for negative numbers, leading to a stack overflow.
* **Unconverted Input:** The `input()` function returns a string, which cannot be used in mathematical operations directly.
