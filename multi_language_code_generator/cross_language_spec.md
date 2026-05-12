# Cross-Language Specification - Student Grade Analyzer

## Algorithm
Parse a list of student records and compute:
- Total number of students
- Class average score
- Highest and lowest scores
- Grade distribution (A, B, C, D, F)
- List of students who failed (score below 50)

## Inputs
A list of student records in JSON format, where each record contains:
- name (string): the student full name
- score (integer): the student numeric score between 0 and 100

Example input:
[
  {"name": "Alice", "score": 92},
  {"name": "Bob", "score": 45},
  {"name": "Carol", "score": 78}
]

## Outputs
A JSON object containing:
- total_students (integer): total number of students processed
- average_score (float): arithmetic mean of all scores rounded to 2 decimal places
- highest_score (integer): maximum score in the dataset
- lowest_score (integer): minimum score in the dataset
- grade_distribution (object): count of students per grade (A, B, C, D, F)
- failed_students (list): names of students who scored below 50

## Grade Scale
- A: 90 to 100
- B: 75 to 89
- C: 60 to 74
- D: 50 to 59
- F: below 50

## Edge Cases
- Empty input list: return zeros and empty lists for all fields
- Single student: average equals that student score
- All students failing: failed_students contains all names
- All students with perfect score: average is 100.0, all grades are A
- Score of exactly 50: classified as D, not F

## Test Cases

### Test Case 1 - Normal mixed input
Input: Alice=92, Bob=45, Carol=78, David=55, Eve=88
Expected Output:
- total_students: 5
- average_score: 71.60
- highest_score: 92
- lowest_score: 45
- grade_distribution: A=1, B=2, C=0, D=1, F=1
- failed_students: [Bob]

### Test Case 2 - Empty input
Input: []
Expected Output:
- total_students: 0
- average_score: 0.00
- highest_score: 0
- lowest_score: 0
- grade_distribution: A=0, B=0, C=0, D=0, F=0
- failed_students: []

### Test Case 3 - Single student passing
Input: Alice=85
Expected Output:
- total_students: 1
- average_score: 85.00
- highest_score: 85
- lowest_score: 85
- grade_distribution: A=0, B=1, C=0, D=0, F=0
- failed_students: []

### Test Case 4 - All students failing
Input: Alice=30, Bob=20, Carol=45
Expected Output:
- total_students: 3
- average_score: 31.67
- highest_score: 45
- lowest_score: 20
- grade_distribution: A=0, B=0, C=0, D=0, F=3
- failed_students: [Alice, Bob, Carol]

### Test Case 5 - Boundary score of exactly 50
Input: Alice=50, Bob=89, Carol=90
Expected Output:
- total_students: 3
- average_score: 76.33
- highest_score: 90
- lowest_score: 50
- grade_distribution: A=1, B=1, C=0, D=1, F=0
- failed_students: []
