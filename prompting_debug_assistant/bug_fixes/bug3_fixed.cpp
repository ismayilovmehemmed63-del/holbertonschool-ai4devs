#include <iostream>
using namespace std;

int* createArray(int n) {
    int* arr = new int[n];
    for(int i = 0; i < n; i++) {
        arr[i] = i * 10;
    }
    return arr;
}

int main() {
    int n = 5;
    int* ptr = createArray(n);
    for(int i = 0; i < n; i++) {
        cou

cat > bug4_fixed.py << 'EOF'
def factorial(n):
    if n < 0:
        return "Negative numbers are not allowed"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print(f"Factorial of 5 is: {factorial(5)}")

# Tests
assert factorial(5) == 120
assert factorial(0) == 1
assert factorial(1) == 1
print("All tests passed!")
