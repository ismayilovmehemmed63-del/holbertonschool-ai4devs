## Bug 1 – bug1.py
*   **Intended Behavior**: The function should calculate the average of a list of numbers. It must sum all elements and divide by the total count, ensuring it returns 0 for empty lists to prevent division errors.
*   **Issue Type**: Syntax Error / Runtime Exception.
*   **Notes**: 
    *   Missing a colon (`:`) at the end of the function definition.
    *   No empty list check, causing a `ZeroDivisionError`.

---

## Bug 2 – bug2.js
*   **Intended Behavior**: The script is intended to retrieve user profile data asynchronously and log the name and role. It must ensure the asynchronous operation completes before accessing properties.
*   **Issue Type**: Logical Error / Async-Await Misuse.
*   **Notes**: 
    *   The `await` keyword is missing when calling `fetchUserData()`.
    *   The variable `user` remains a `Promise`, making `.name` and `.role` return `undefined`.

---

## Bug 3 – bug3.cpp
*   **Intended Behavior**: The program should allocate a dynamic array, initialize its values, and print each element within the valid index range of 0 to n-1.
*   **Issue Type**: Runtime Exception / Memory Access Error.
*   **Notes**: 
    *   The loop condition `i <= n` is an off-by-one error.
    *   Accessing index 5 in a 5-element array leads to a segmentation fault.

---

## Bug 4 – bug4.py
*   **Intended Behavior**: The function should calculate the factorial of a number `n` by multiplying all positive integers from 1 up to and including `n` (e.g., 5! = 120).
*   **Issue Type**: Logical Error / Off-by-one Error.
*   **Notes**: 
    *   The `range(1, n)` loop excludes the value `n` itself.
    *   As a result, `factorial(5)` incorrectly returns 24 instead of 120.
