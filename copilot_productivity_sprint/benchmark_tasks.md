# Benchmark Tasks – Copilot Productivity Sprint

## Task 1 - String Manipulation Function
**Requirements**: Implement a function that takes a string and returns it reversed, with all vowels removed and first letter of each word capitalized.
**Inputs**: A plain string (e.g. "hello world")
**Outputs**: Transformed string (e.g. "Hll Wrld" reversed)
**Acceptance Criteria**:
- Function handles empty string input by returning empty string
- All vowels (a, e, i, o, u) are removed case-insensitively
- Returns correct result for single word and multi-word strings
- Includes at least 3 unit tests using pytest

---

## Task 2 - REST API Endpoint
**Requirements**: Implement a POST /users endpoint using Flask with input validation.
**Inputs**: JSON body { "name": string, "email": string }
**Outputs**: JSON response with stored user object including generated ID
**Acceptance Criteria**:
- Returns 201 status code on successful user creation
- Returns 400 status code if email format is invalid
- Returns 400 status code if name or email fields are missing
- User is assigned a unique integer ID automatically

---

## Task 3 - Data Processing Script
**Requirements**: Write a Python script that reads a list of student scores, calculates statistics, and identifies pass/fail status.
**Inputs**: A list of dictionaries with student name and score (e.g. [{"name": "Alice", "score": 85}])
**Outputs**: Printed report showing each student's name, score, status (Pass/Fail), class average, highest score, and lowest score
**Acceptance Criteria**:
- Pass threshold is 50 points
- Correctly calculates average, min, and max scores
- Handles empty list input without crashing
- Output is clearly formatted and readable
