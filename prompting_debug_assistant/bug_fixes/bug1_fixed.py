def calculate_average(numbers):
    if len(numbers) == 0:
        print("The list is empty!")
        return 0
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"Average value: {result}")

# Tests
assert calculate_average([10, 20, 30]) == 20
assert calculate_average([]) == 0
print("All tests passed!")
