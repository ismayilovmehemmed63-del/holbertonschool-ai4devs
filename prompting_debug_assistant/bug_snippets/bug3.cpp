#include <iostream>

int* createArray(int size) {
    // Xəta: Lokal massiv (stack) funksiya bitəndə silinir
    // Onu pointer kimi qaytarmaq təhlükəlidir (Dangling Pointer)
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
    // Xəta: Silinmiş yaddaşa müraciət (Segmentation Fault ehtimalı)
    for(int i = 0; i <= n; i++) { // Həmçinin n+1 dəfə dövr edir (out of bounds)
        std::cout << "Index " << i << ": " << myPtr[i] << std::endl;
    }

    return 0;
}
