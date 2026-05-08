def calculate_average(numbers):
    # Xəta: Boş siyahı daxil olsa ZeroDivisionError verəcək
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    
    average = total / len(numbers)
    return average

def get_last_n_elements(items, n):
    # Xəta: Off-by-one (indeks xətası). n = len(items) olsa xəta verə bilər
    # Və ya dilimləmə (slicing) məntiqi səhvdir
    result = []
    start_index = len(items) - n
    for i in range(start_index, len(items) + 1): 
        result.append(items[i])
    return result

# Test
my_list = [10, 20, 30, 40, 50]
print("Average:", calculate_average(my_list))

# Siyahı boş olsa nə olar?
# print(calculate_average([])) 

print("Last 3 items:", get_last_n_elements(my_list, 3))
