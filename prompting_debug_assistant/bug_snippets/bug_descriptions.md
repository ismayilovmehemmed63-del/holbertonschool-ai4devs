## Bug 1 – bug1.py

*   **Intended Behavior**: 
    The function `calculate_average(numbers)` is intended to calculate the mean value of a list. It should sum all elements and divide by the count, returning 0 if the list is empty to prevent errors.

*   **Issue Type**: 
    Syntax Error / Runtime Exception (Division by Zero)

*   **Notes**: 
    *   **Syntax**: The function definition is missing a colon (`:`) at the end.
    *   **Logic**: There is no guard clause for an empty list, which leads to a division by zero if the input is `[]`.

---

## Bug 2 – bug2.js

*   **Intended Behavior**: 
    The script should fetch user data from a simulated API asynchronously. The `displayDashboard` function must wait for the data resolution to log the user's name and role correctly.

*   **Issue Type**: 
    Logical Error / Async-Await Misuse

*   **Notes**: 
    *   **Specific Issue**: The `await` keyword was omitted when calling `fetchUserData()`.
    *   **Result**: The variable `user` receives a `Promise` instead of the data, causing `user.name` to be `undefined`.

---

## Bug 3 – bug3.cpp

*   **Intended Behavior**: 
    The program should allocate a dynamic array of size `n`, populate it with values, print each element within the valid index range (0 to n-1), and then deallocate the memory.

*   **Issue Type**: 
    Runtime Exception / Out-of-Bounds Access

*   **Notes**: 
    *   **Specific Issue**: The loop uses `<= n` instead of `< n`, attempting to access an index outside the allocated memory.
    *   **Consequence**: This causes a segmentation fault or memory corruption during runtime.

---

## Bug 4 – bug4.py

*   **Intended Behavior**: 
    The `factorial` function should return the product of all positive integers up to and including `n`. For `factorial(5)`, the output should be exactly 120.

*   **Issue Type**: 
    Logical Error / Off-by-one Error

*   **Notes**: 
    *   **Specific Issue**: The loop uses `range(1, n)`, which excludes the value of `n`.
    *   **Result**: The product is missing the final multiplier, resulting in 24 instead of 120. Using `range(1, n + 1)` is required.
