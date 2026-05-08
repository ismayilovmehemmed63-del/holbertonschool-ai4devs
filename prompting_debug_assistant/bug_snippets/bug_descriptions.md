# Bug Descriptions - Debugging Task

## Bug 1
**File Name:** bug1.py
**Intended Behavior:** The code should compute the average of a list of integers. It must include a validation step to return 0 or handle the case where the list is empty. Additionally, it should slice the list correctly without index overflow.
**Issue Type:** Logic Error / ZeroDivisionError.
**Detailed Notes:** The script fails when an empty list is provided because it divides by zero. Also, the loop boundary in the slicing function exceeds the list range by 1.

## Bug 2
**File Name:** bug2.js
**Intended Behavior:** This script should fetch data from a source and wait for the result to be stored in the 'user' variable before trying to access its attributes. A promise or async/await should be used to manage the timing.
**Issue Type:** Asynchronous Execution Error.
**Detailed Notes:** The dashboard displays data before it is actually fetched, causing it to read properties of 'null'. This happens because the function returns immediately while the timeout is still running.

## Bug 3
**File Name:** bug3.cpp
**Intended Behavior:** The goal is to allocate an array that remains accessible throughout the program's lifecycle and iterate through it safely using defined boundaries.
**Issue Type:** Memory Safety / Segmentation Fault.
**Detailed Notes:** The function returns a pointer to a local stack-allocated array which is destroyed upon exit. The loop in the main function also attempts to access an out-of-bounds index.

## Bug 4
**File Name:** bug4.py
**Intended Behavior:** The program should convert user input into an integer and recursively calculate its factorial. It should have a base case to prevent negative numbers from triggering infinite recursion.
**Issue Type:** Recursion Error / Type Mismatch.
**Detailed Notes:** Input is captured as a string and never converted to an integer, making math impossible. Furthermore, negative inputs lead to infinite recursive calls, causing a stack overflow.
