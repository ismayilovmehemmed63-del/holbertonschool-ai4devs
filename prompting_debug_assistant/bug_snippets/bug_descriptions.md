Başa düşdüm, başlıqların önündəki `##` işarələrini sildim və strukturu sistemin tələb etdiyi tam dəqiqliklə yenidən hazırladım.

Bu variantı kopyalayaraq istifadə edə bilərsən:

---

Bug 1 – bug1.py

* **Intended Behavior**:
The function `calculate_average(numbers)` should accept a list of numbers, sum them correctly, and return the arithmetic mean. It should also include a check to handle empty lists by returning 0 to avoid division by zero.
* **Issue Type**:
* Syntax Error
* Logical Error (ZeroDivisionError)


* **Notes**:
* **Specific Error**: The function definition `def calculate_average(numbers)` is missing a colon (`:`) at the end.
* **Consequence**: This causes a `SyntaxError`, and the Python script fails to compile or run.
* **Logic Flaw**: There is no validation to check if the list is empty before dividing by its length, which would cause a crash at runtime.



---

Bug 2 – bug2.js

* **Intended Behavior**:
This script is intended to fetch user data asynchronously. The `displayDashboard` function should use `await` to pause execution until the `fetchUserData` promise resolves, ensuring the user's name and role are correctly logged.
* **Issue Type**:
* Logical Error
* Async/Await Mismanagement


* **Notes**:
* **Specific Error**: The `await` keyword is missing when calling `fetchUserData()`.
* **Consequence**: The `user` variable is assigned a `Promise` object instead of the actual data object.
* **Outcome**: The console logs `undefined` for `user.name` and `user.role` because these properties do not exist on a pending Promise object.



---

Bug 3 – bug3.cpp

* **Intended Behavior**:
The program should allocate a dynamic integer array of size `n`, fill it with values, and iterate from index `0` to `n-1` to print them. Finally, it must free the allocated memory to ensure no leaks.
* **Issue Type**:
* Runtime Exception
* Out-of-Bounds Memory Access


* **Notes**:
* **Specific Error**: The loop condition `i <= n` is an off-by-one error.
* **Consequence**: In C++, an array of size 5 only has valid indices from 0 to 4. The loop attempts to access `ptr[5]`.
* **Outcome**: Accessing memory outside the allocated block leads to a segmentation fault or unpredictable runtime crashes.



---

Bug 4 – bug4.py

* **Intended Behavior**:
The script should calculate the factorial of a number `n` by multiplying all integers from 1 up to and including `n`. For input 5, the expected output is 120.
* **Issue Type**:
* Logical Error
* Off-by-one Error (Range Limit)


* **Notes**:
* **Specific Error**: The `for` loop uses `range(1, n)`.
* **Consequence**: Python's `range(start, stop)` function is exclusive of the `stop` value, meaning the loop ends at `n-1`.
* **Outcome**: The calculation excludes the multiplier `n` itself. For example, `factorial(5)` returns 24 instead of 120. This is fixed by using `range(1, n + 1)`.
