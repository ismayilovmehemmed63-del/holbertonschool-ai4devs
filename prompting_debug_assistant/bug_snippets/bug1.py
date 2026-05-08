def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    total = 0
    for i in range(len(numbers)):
        total += numbers[i]

    average = total / len(numbers)
    return average


def get_last_n_elements(items, n):
    result = []

    for i in range(len(items) - n, len(items)):
        result.append(items[i])

    return result


my_list = [10, 20, 30, 40, 50]
print(calculate_average(my_list))
print(get_last_n_elements(my_list, 3))
