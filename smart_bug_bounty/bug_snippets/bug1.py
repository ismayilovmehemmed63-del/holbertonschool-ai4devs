def calculate_discount(price, discount_percent):
    if discount_percent > 100:
        return 'Invalid discount'
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price

def get_top_students(students, n):
    sorted_students = sorted(students, key=lambda x: x['score'])
    return sorted_students[:n]

prices = [100, 200, 300]
for p in prices:
    print(calculate_discount(p, 20))

students = [
    {'name': 'Alice', 'score': 92},
    {'name': 'Bob', 'score': 78},
    {'name': 'Carol', 'score': 88}
]
print(get_top_students(students, 2))
