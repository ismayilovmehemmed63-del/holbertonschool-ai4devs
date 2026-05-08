def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    
    average = total / len(numbers)
    return average

def get_last_n_elements(items, n):
    result = []
    start_index = len(items) - n
    for i in range(start_index, len(items) + 1): 
        result.append(items[i])
    return result
my_list = [10, 20, 30, 40, 50]
print("Average:", calculate_average(my_list))
print("Last 3 items:", get_last_n_elements(my_list, 3))
