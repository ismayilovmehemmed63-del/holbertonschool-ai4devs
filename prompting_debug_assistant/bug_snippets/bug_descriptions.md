# Project: Prompting Debug Assistant - Bug Descriptions

This document outlines the intended behavior and known issues for the buggy code snippets provided in the `bug_snippets/` directory. These snippets are designed for AI-assisted debugging practice.

---

## Bug 1 – bug1.py
**Intended Behavior**:  
The script is supposed to calculate the average of a list of numbers and then return the last `n` elements from that list. The `calculate_average` function should handle any list of numbers, and the `get_last_n_elements` function should return a specific slice of the list.

**Issue Type**: Logical Error / Off-by-one Error / Runtime Exception.  
**Detailed Notes**:
*   **Division by Zero**: The `calculate_average` function does not check if the list is empty, leading to a crash if `len(numbers)` is zero.
*   **Off-by-one**: In `get_last_n_elements`, the loop range `range(start_index, len(items) + 1)` will attempt to access an index that is out of bounds, causing an `IndexError`.
*   **Logic**: The manual slicing logic is more complex than necessary, making it prone to errors.

---

## Bug 2 – bug2.js
**Intended Behavior**:  
This JavaScript snippet simulates fetching user data from a remote server (using a timeout) and then displaying that data on a dashboard. The goal is to ensure the dashboard waits for the data before trying to access its properties.

**Issue Type**: Asynchronous Execution Error.  
**Detailed Notes**:
*   **Async/Await Mismanagement**: The `fetchUserData` function returns the `user` variable immediately before the `setTimeout` callback has a chance to update it.
*   **Null Pointer Reference**: Because the function returns `null` immediately, the `displayDashboard` function tries to read `.name` and `.role` from a null object, resulting in a "TypeError: Cannot read property 'name' of null."

---

## Bug 3 – bug3.cpp
**Intended Behavior**:  
The C++ program aims to dynamically (or locally) create an array of integers, populate it with values (multiples of 10), and print these values to the console using pointers.

**Issue Type**: Memory Management / Segmentation Fault.  
**Detailed Notes**:
*   **Dangling Pointer**: The function `createArray` defines a local array on the stack. When the function returns, that memory is deallocated, leaving the pointer in `main` pointing to invalid memory.
*   **Out-of-Bounds Access**: The loop in `main` uses `i <= n`, which tries to access the 6th element of a 5-element array.
*   **Memory Safety**: The code fails to use `new` for heap allocation, which is required if a pointer to a local array needs to persist outside its scope.

---

## Bug 4 – bug4.py
**Intended Behavior**:  
The script should take a numerical input from the user, calculate its factorial using a recursive function, and print the result as a string.

**Issue Type**: Recursion Error / Type Mismatch.  
**Detailed Notes**:
*   **Infinite Recursion**: The `factorial` function lacks a check for negative numbers. If a negative value is passed, it will trigger a `RecursionError` (Stack Overflow).
*   **Input Handling**: The `input()` function in Python 3 returns a string. The code fails to convert this string to an integer before passing it to the math function, causing a `TypeError`.
*   **String Concatenation**: The code attempts to add a non-string result to a string in the print statement without explicit casting.

