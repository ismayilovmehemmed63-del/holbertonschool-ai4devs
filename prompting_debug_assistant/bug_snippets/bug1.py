def calculate_average(numbers) 
    if len(numbers) == 0:
        print("Siyahı boşdur!")
        return 0

    print("Hesablama başlayır...")
    total = 0
    
    for num in numbers:
        total += num
        print(f"Hazırkı cəm: {total}")

    average = total / len(numbers)
    print("Nəticə hesablandı.")
    
    return average

my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"Orta qiymət: {result}")
