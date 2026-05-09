## Bug 1 – bug1.py
Intended Behavior: The calculate_average function is designed to take a list of numbers, sum them up, and return their arithmetic mean. It should also handle empty lists gracefully to avoid mathematical errors.

Issue Type: Syntax Error & Potential Runtime Exception.

Notes:

Primary Issue: The function header def calculate_average(numbers) is missing the required colon (:), which is a fatal syntax violation in Python.

Secondary Issue: The logic lacks a check for len(numbers) == 0, which would trigger a ZeroDivisionError during execution if an empty list were passed.

## Bug 2 – bug2.js
Intended Behavior: The displayDashboard function should wait for the asynchronous fetchUserData function to resolve and then log the user's name and role to the console.

Issue Type: Logical Error (Asynchronous Programming Misuse).

Notes:

The Flaw: The developer omitted the await keyword before fetchUserData().

The Consequence: JavaScript does not wait for the 2000ms timer; instead, it assigns a pending Promise object to the user variable. Since a Promise object does not have .name or .role properties, the output results in undefined.

## Bug 3 – bug3.cpp
Intended Behavior: The program should allocate memory for an integer array on the heap, populate it, print all elements from index 0 to n-1, and finally release the memory to prevent leaks.

Issue Type: Runtime Exception (Memory Management & Segmentation Risk).

Notes:

Off-by-one Boundary: The loop condition i <= n is incorrect for an array of size n. In C++, indices are zero-based, so for n=5, only indices 0, 1, 2, 3, and 4 are valid.

The Crash: Accessing ptr[5] leads to an "Out of Bounds" error, which causes the program to access unallocated memory, typically resulting in a segmentation fault.

## Bug 4 – factorial_bug.py
Intended Behavior: The script aims to calculate the factorial of a positive integer (n!) using an iterative loop, ensuring that every number from 1 to n is included in the product.

Issue Type: Logical Error (Off-by-one in Range).

Notes:

Range Limitation: The range(1, n) function generates sequence values up to, but not including, the upper limit (n).

Mathematical Impact: For num = 5, the loop only multiplies 1 * 2 * 3 * 4. The missing final multiplication results in 24 instead of the correct value of 120. This is a classic logic error where the loop termination condition is incorrectly defined.
