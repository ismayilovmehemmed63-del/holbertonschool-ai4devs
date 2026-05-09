## Bug 1 – bug1.py

*   **Intended Behavior**: The script is designed to compute the average of a list. It should verify if the list is not empty, calculate the sum of elements, and return the mean. If the list is empty, it should return 0 to maintain stability.
*   **Issue Type**: Critical Syntax Error and Unhandled Runtime Exception (ZeroDivisionError).
*   **Notes**: 
    *   The function header is missing the mandatory colon (`:`) required by Python syntax.
    *   The code lacks a conditional check for an empty list, which leads to a division by zero error when the list length is 0.

---

## Bug 2 – bug2.js

*   **Intended Behavior**: This JavaScript function is intended to fetch user credentials from an asynchronous data source. It must successfully await the promise resolution before attempting to access and log the object's properties.
*   **Issue Type**: Asynchronous Programming Logical Error (Missing Await Keyword).
*   **Notes**: 
    *   The `fetchUserData` call is made without the `await` keyword inside an `async` function.
    *   This causes the script to treat the variable as a Promise object rather than the resolved data, resulting in `undefined` values during logging.

---

## Bug 3 – bug3.cpp

*   **Intended Behavior**: The C++ program should safely allocate memory for an array of size `n`, populate it with integers, and print elements specifically from index 0 to index `n-1` to remain within allocated memory bounds.
*   **Issue Type**: Memory Access Violation and Runtime Runtime Exception (Out of Bounds).
*   **Notes**: 
    *   The loop condition `i <= n` incorrectly allows the iteration to reach the index equal to the array size.
    *   In a zero-indexed system, this causes an "off-by-one" error, attempting to access unallocated memory which leads to a segmentation fault.

---

## Bug 4 – bug4.py

*   **Intended Behavior**: The function is intended to return the factorial of a number `n`. It should multiply every integer starting from 1 up to and including the value of `n` to provide a mathematically correct result.
*   **Issue Type**: Logical Loop Error and Off-by-one Boundary Condition.
*   **Notes**: 
    *   The `range(1, n)` function stops the loop at `n-1`, failing to include the final multiplier.
    *   For an input of 5, the result is 24 instead of 120; this logic error requires changing the range to `range(1, n + 1)`.
      
