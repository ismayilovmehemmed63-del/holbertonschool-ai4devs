def calculate_average(numbers) 
    if len(numbers) == 0:
        print("The list is empty!")
        return 0

    print("Calculation starting...")
    total = 0
    
    for num in numbers:
        total += num
        print(f"Current sum: {total}")

    average = total / len(numbers)
    print("Result calculated.")
    
    return average

my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"Average value: {result}")
