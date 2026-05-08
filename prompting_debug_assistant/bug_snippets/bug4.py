def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def process_input():
    user_val = input("Enter a number for factorial: ")
    result = factorial(user_val)
    print("Result is: " + result)

try:
    process_input()
except Exception as e:
    print(f"Oops! Something went wrong: {e}")
