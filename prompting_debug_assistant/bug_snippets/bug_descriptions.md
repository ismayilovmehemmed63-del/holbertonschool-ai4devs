1. File: bug1.py
Intended Behavior: The calculate_average function should return the mean of a list and return 0 if the list is empty. The get_last_n_elements function should return the last n elements using safe, zero-based indices.

Issue Type: ZeroDivisionError and IndexError.

Root Cause: The code lacks a check for empty lists, leading to division by zero. In the slicing function, the range goes to len(items) + 1, which is an out-of-bounds index.

Solution: Add if not numbers: return 0 and change the loop range to len(items).

2. File: bug2.js
Intended Behavior: The script should fetch user data asynchronously and ensure the user object is populated before the dashboard attempts to access its name and role properties.

Issue Type: Asynchronous Logic Error (Race Condition).

Root Cause: fetchUserData returns null immediately because setTimeout is non-blocking. displayDashboard tries to read properties from null before the data is received.

Solution: Use async/await or a Promise to wait for the server response before calling the display function.

3. File: bug3.cpp
Intended Behavior: The program should allocate memory for an array that persists outside the function scope, and the loop in main should iterate within the defined array size (0 to n-1).

Issue Type: Memory Safety (Dangling Pointer) and Buffer Overflow.

Root Cause: The function returns a pointer to a local stack-allocated array that is destroyed on return. The loop condition i <= n accesses memory outside the array's bounds.

Solution: Use dynamic memory allocation (new int[size]) and change the loop condition to i < n.

4. File: bug4.py
Intended Behavior: The script should take a numerical string, convert it to an integer, and calculate the factorial. It should also include a check for negative numbers to prevent infinite recursion.

Issue Type: TypeError and RecursionError.

Root Cause: input() returns a string, causing a TypeError in math operations. Negative values cause infinite recursion because they never reach the base case n == 0.

Solution: Wrap the input in int() and add a condition to handle negative inputs safely.
