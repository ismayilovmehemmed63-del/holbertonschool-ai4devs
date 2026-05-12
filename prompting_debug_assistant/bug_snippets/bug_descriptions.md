## Bug 1 - bug1.py

*   **Intended Behavior**: 
    The `calculate_average` function is intended to safely calculate the arithmetic mean of a numeric list. It must include robust error handling by first validating if the input list is empty; if the list is empty, it should return a default value of 0 to prevent program crashes. For non-empty lists, it must correctly sum all elements and return the total divided by the number of elements.

*   **Issue Type**: 
    Syntax Error and Missing Input Validation (ZeroDivisionError).

*   **Notes**: 
    *   **Syntax**: The function header `def calculate_average(numbers)` is missing the mandatory colon (`:`) required by Python.
    *   **Logic**: The script lacks a guard clause to handle empty list inputs, which results in a `ZeroDivisionError` during the division step when `len(numbers)` is zero.

---

## Bug 2 - bug2.js

*   **Intended Behavior**: 
    The `displayDashboard` function is intended to manage asynchronous data retrieval from a promise-based source. It must use the `await` keyword to pause execution until the `fetchUserData` promise is fully resolved. This ensures the resulting user object is available so that properties like `name` and `role` can be accessed and logged without returning undefined.

*   **Issue Type**: 
    Asynchronous Flow Control Error (Missing Await).

*   **Notes**: 
    *   **Specific Issue**: The `await` keyword was omitted during the call to `fetchUserData()`, causing the code to proceed with a pending Promise object.
    *   **Consequence**: Since the logging happens before resolution, the script attempts to read properties from the Promise itself, leading to `undefined` outputs.

---

## Bug 3 - bug3.cpp

*   **Intended Behavior**: 
    This program is designed to allocate and manage heap memory for an integer array of size `n`. The intended logic is to iterate through the array using a strictly less-than boundary (`i < n`) to access indices 0 through `n-1`. Finally, the program must release the allocated memory using `delete[]` to prevent memory leaks and ensure system stability.

*   **Issue Type**: 
    Off-by-one Error and Illegal Memory Access (Segmentation Fault).

*   **Notes**: 
    *   **Specific Issue**: The loop condition `i <= n` in the `main` function incorrectly allows the iteration to reach index 5 in a 5-element array.
    *   **Result**: Accessing index `ptr[5]` is an out-of-bounds operation in C++, which triggers a segmentation fault or undefined runtime behavior.

---

## Bug 4 - bug4.py

*   **Intended Behavior**: 
    The `factorial` function is intended to return the mathematical product of all positive integers from 1 up to and including the input `n`. It should handle the base cases correctly, such as returning 1 for inputs of 0 or 1, and ensure the iterative loop encompasses the entire range including the terminal value `n`.

*   **Issue Type**: 
    Logical Boundary Condition Error (Off-by-one in Range).

*   **Notes**: 
    *   **Specific Issue**: The function uses `range(1, n)`, which is exclusive of the stop value `n` in Python.
    *   **Consequence**: For an input of 5, the loop only multiplies $1 \times 2 \times 3 \times 4$, resulting in 24 instead of the correct factorial value of 120. The range should be defined as `range(1, n + 1)`.
