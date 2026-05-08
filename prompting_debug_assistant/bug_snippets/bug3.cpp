#include <iostream>
#include <vector>
int* createArray(int size) {
    int arr[size]; 
    for(int i = 0; i < size; i++) {
        arr[i] = i * 10;
    }
    return arr; 
}

int main() {
    int n = 5;
    int* myPtr = createArray(n);  
    std::cout << "Array elements: " << std::endl;
    for(int i = 0; i <= n; i++) {
        std::cout << "Index " << i << ": " << myPtr[i] << std::endl;
    }
    return 0;
}
