def factorial(n):
    if n < 0:
        return "Negative numbers are not allowed"
    
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(1, n):
        result = result * i
        print(f"Multiplying by {i}, current result: {result}")

    print("Calculation finished.")
    return result

num = 5
print(f"Factorial of {num} is: {factorial(num)}")
