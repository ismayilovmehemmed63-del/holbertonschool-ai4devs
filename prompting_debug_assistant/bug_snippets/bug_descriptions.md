##Bug 1 – bug1.py
Intended Behavior: Calculate the average of a list of numbers.
Issue Type: Syntax Error.
Notes: The function definition is missing a colon (:) at the end of the line, which causes a complete failure to execute.

##Bug 2 – bug2.js
Intended Behavior: Fetch user data from an API and display the name and role.
Issue Type: Logical Error (Async/Await Misuse).
Notes: The await keyword was omitted, so the script tries to read properties from a Promise object rather than the resolved data, resulting in undefined.

##Bug 3 – bug3.cpp
Intended Behavior: Iterate through a dynamically allocated array and print its values.
Issue Type: Runtime Exception (Out of Bounds).
Notes: The loop condition uses <= instead of <, causing the program to access memory outside the array's range (index 5 of 5), leading to a crash.

##Bug 4 – bug4.py
Intended Behavior: Calculate the mathematical factorial of a number n.
Issue Type: Off-by-one error.
Notes: The range(1, n) loop stops one step early and excludes the actual number n from the multiplication, producing an incorrect result.
