# Bug Descriptions

## bug1.py
- **Intended Behavior**: Calculate discounted price and return top N students sorted by highest score.
- **Current Issue**: get_top_students() sorts in ascending order instead of descending, returning the lowest scoring students instead of the top performers.

## bug2.js
- **Intended Behavior**: Calculate total price of all items and find a user by ID.
- **Current Issue**: Loop condition uses <= instead of <, causing an off-by-one error that accesses an undefined index and throws a TypeError. Also, findUser() returns undefined instead of null when user is not found.

## bug3.java
- **Intended Behavior**: A bank account class that supports deposit and withdrawal operations.
- **Current Issue**: The deposit() method uses =+ instead of +=, which assigns a positive value instead of adding to the balance, causing incorrect balance calculations.

## bug4.c
- **Intended Behavior**: Copy user input into a buffer and perform integer division.
- **Current Issue**: Buffer overflow vulnerability because strcpy() does not check input length against buffer size. Division by zero error when divide() is called with 0 as the second argument.

## bug5.py
- **Intended Behavior**: Read a file safely, parse configuration strings, and connect to a database securely.
- **Current Issue**: File is opened without a context manager or error handling, causing resource leaks. parse_config() crashes if a line has no equals sign. Database password is hardcoded in the connection string instead of using environment variables.
