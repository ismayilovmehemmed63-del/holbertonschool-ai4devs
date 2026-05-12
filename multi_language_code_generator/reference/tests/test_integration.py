import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grade_analyzer import analyze_grades

def test_two_students_average():
    students = [
        {'name': 'Alice', 'score': 60},
        {'name': 'Bob', 'score': 80}
    ]
    result = analyze_grades(students)
    assert result['average_score'] == 70.00

def test_no_failed_students():
    students = [
        {'name': 'Alice', 'score': 55},
        {'name': 'Bob', 'score': 75}
    ]
    result = analyze_grades(students)
    assert result['failed_students'] == []

def test_total_students_count():
    students = [{'name': f'S{i}', 'score': 70} for i in range(10)]
    result = analyze_grades(students)
    assert result['total_students'] == 10

def test_all_grades_present():
    students = [
        {'name': 'A', 'score': 95},
        {'name': 'B', 'score': 80},
        {'name': 'C', 'score': 65},
        {'name': 'D', 'score': 52},
        {'name': 'F', 'score': 30}
    ]
    result = analyze_grades(students)
    for grade in ['A', 'B', 'C', 'D', 'F']:
        assert result['grade_distribution'][grade] == 1

def test_score_exactly_90_is_A():
    result = analyze_grades([{'name': 'Alice', 'score': 90}])
    assert result['grade_distribution']['A'] == 1
    assert result['grade_distribution']['B'] == 0

if __name__ == '__main__':
    test_two_students_average()
    test_no_failed_students()
    test_total_students_count()
    test_all_grades_present()
    test_score_exactly_90_is_A()
    print('All integration tests passed!')
