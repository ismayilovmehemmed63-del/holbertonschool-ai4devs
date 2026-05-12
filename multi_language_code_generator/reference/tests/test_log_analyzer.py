import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grade_analyzer import analyze_grades

def test_normal_mixed_input():
    students = [
        {'name': 'Alice', 'score': 92},
        {'name': 'Bob', 'score': 45},
        {'name': 'Carol', 'score': 78},
        {'name': 'David', 'score': 55},
        {'name': 'Eve', 'score': 88}
    ]
    result = analyze_grades(students)
    assert result['total_students'] == 5
    assert result['average_score'] == 71.60
    assert result['highest_score'] == 92
    assert result['lowest_score'] == 45
    assert result['grade_distribution'] == {'A': 1, 'B': 2, 'C': 0, 'D': 1, 'F': 1}
    assert result['failed_students'] == ['Bob']

def test_empty_input():
    result = analyze_grades([])
    assert result['total_students'] == 0
    assert result['average_score'] == 0.00
    assert result['highest_score'] == 0
    assert result['lowest_score'] == 0
    assert result['failed_students'] == []

def test_single_student_passing():
    result = analyze_grades([{'name': 'Alice', 'score': 85}])
    assert result['total_students'] == 1
    assert result['average_score'] == 85.00
    assert result['grade_distribution']['B'] == 1
    assert result['failed_students'] == []

def test_all_students_failing():
    students = [
        {'name': 'Alice', 'score': 30},
        {'name': 'Bob', 'score': 20},
        {'name': 'Carol', 'score': 45}
    ]
    result = analyze_grades(students)
    assert result['total_students'] == 3
    assert result['grade_distribution']['F'] == 3
    assert set(result['failed_students']) == {'Alice', 'Bob', 'Carol'}

def test_boundary_score_50():
    students = [
        {'name': 'Alice', 'score': 50},
        {'name': 'Bob', 'score': 89},
        {'name': 'Carol', 'score': 90}
    ]
    result = analyze_grades(students)
    assert result['grade_distribution']['D'] == 1
    assert result['grade_distribution']['F'] == 0
    assert 'Alice' not in result['failed_students']

def test_all_perfect_scores():
    students = [
        {'name': 'Alice', 'score': 100},
        {'name': 'Bob', 'score': 100}
    ]
    result = analyze_grades(students)
    assert result['average_score'] == 100.00
    assert result['grade_distribution']['A'] == 2
    assert result['failed_students'] == []

def test_single_failing_student():
    result = analyze_grades([{'name': 'Bob', 'score': 30}])
    assert result['failed_students'] == ['Bob']
    assert result['grade_distribution']['F'] == 1

def test_grade_boundaries():
    students = [
        {'name': 'A_student', 'score': 90},
        {'name': 'B_student', 'score': 75},
        {'name': 'C_student', 'score': 60},
        {'name': 'D_student', 'score': 50},
        {'name': 'F_student', 'score': 49}
    ]
    result = analyze_grades(students)
    assert result['grade_distribution'] == {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'F': 1}

def test_large_class():
    students = [{'name': f'Student_{i}', 'score': i % 101} for i in range(50)]
    result = analyze_grades(students)
    assert result['total_students'] == 50

def test_average_calculation():
    students = [
        {'name': 'Alice', 'score': 70},
        {'name': 'Bob', 'score': 80},
        {'name': 'Carol', 'score': 90}
    ]
    result = analyze_grades(students)
    assert result['average_score'] == 80.00

if __name__ == '__main__':
    test_normal_mixed_input()
    test_empty_input()
    test_single_student_passing()
    test_all_students_failing()
    test_boundary_score_50()
    test_all_perfect_scores()
    test_single_failing_student()
    test_grade_boundaries()
    test_large_class()
    test_average_calculation()
    print('All 10 tests passed!')
