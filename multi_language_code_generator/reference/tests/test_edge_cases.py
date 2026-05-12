import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grade_analyzer import analyze_grades

def test_score_89_is_B():
    result = analyze_grades([{'name': 'Alice', 'score': 89}])
    assert result['grade_distribution']['B'] == 1

def test_score_74_is_C():
    result = analyze_grades([{'name': 'Bob', 'score': 74}])
    assert result['grade_distribution']['C'] == 1

def test_score_59_is_D():
    result = analyze_grades([{'name': 'Carol', 'score': 59}])
    assert result['grade_distribution']['D'] == 1

def test_highest_and_lowest():
    students = [
        {'name': 'Alice', 'score': 95},
        {'name': 'Bob', 'score': 40},
        {'name': 'Carol', 'score': 70}
    ]
    result = analyze_grades(students)
    assert result['highest_score'] == 95
    assert result['lowest_score'] == 40

def test_multiple_failed_students():
    students = [
        {'name': 'Alice', 'score': 30},
        {'name': 'Bob', 'score': 49},
        {'name': 'Carol', 'score': 95}
    ]
    result = analyze_grades(students)
    assert len(result['failed_students']) == 2
    assert 'Carol' not in result['failed_students']

if __name__ == '__main__':
    test_score_89_is_B()
    test_score_74_is_C()
    test_score_59_is_D()
    test_highest_and_lowest()
    test_multiple_failed_students()
    print('All edge case tests passed!')
