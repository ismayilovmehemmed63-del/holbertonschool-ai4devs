import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grade_analyzer import analyze_grades

def test_case_5():
    students = [{'name': 'Student5', 'score': 50}]
    result = analyze_grades(students)
    assert result['total_students'] == 1

if __name__ == '__main__':
    test_case_5()
    print('Test 5 passed!')
