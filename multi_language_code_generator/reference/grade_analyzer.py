import json

def analyze_grades(students):
    if not students:
        return {
            'total_students': 0,
            'average_score': 0.00,
            'highest_score': 0,
            'lowest_score': 0,
            'grade_distribution': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0},
            'failed_students': []
        }

    total = len(students)
    scores = [s['score'] for s in students]
    average = round(sum(scores) / total, 2)
    highest = max(scores)
    lowest = min(scores)

    grade_distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    failed_students = []

    for student in students:
        score = student['score']
        name = student['name']
        if score >= 90:
            grade_distribution['A'] += 1
        elif score >= 75:
            grade_distribution['B'] += 1
        elif score >= 60:
            grade_distribution['C'] += 1
        elif score >= 50:
            grade_distribution['D'] += 1
        else:
            grade_distribution['F'] += 1
            failed_students.append(name)

    return {
        'total_students': total,
        'average_score': average,
        'highest_score': highest,
        'lowest_score': lowest,
        'grade_distribution': grade_distribution,
        'failed_students': failed_students
    }

if __name__ == '__main__':
    sample = [
        {'name': 'Alice', 'score': 92},
        {'name': 'Bob', 'score': 45},
        {'name': 'Carol', 'score': 78}
    ]
    result = analyze_grades(sample)
    print(json.dumps(result, indent=2))
