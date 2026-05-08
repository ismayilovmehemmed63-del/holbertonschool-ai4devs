#include <iostream>
#include <vector>

int* createArray(int size) {
    // Xəta: Lokal massiv funksiya bitəndə silinir (Dangling Pointer)
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
    
    // Xəta: i <= n olması "Out of bounds" xətası yaradır
    for(int i = 0; i <= n; i++) {
        std::cout << "Index " << i << ": " << myPtr[i] << std::endl;
    }
    
    return 0;
}
