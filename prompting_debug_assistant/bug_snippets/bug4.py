def factorial(n):
    # Xəta: Mənfi ədəd daxil olsa sonsuz rekursiya yaranacaq (RecursionError)
    # Xəta: n integer deyil, string olsa xəta verəcək
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def process_input():
    user_val = input("Enter a number for factorial: ")
    # Xəta: input() həmişə string qaytarır, integer-ə çevrilməyib
    result = factorial(user_val)
    print("Result is: " + result)

# Proqramı başladırıq
try:
    process_input()
except Exception as e:
    print(f"Oops! Something went wrong: {e}")
