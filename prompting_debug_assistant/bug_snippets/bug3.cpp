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
        cout << ptr[i] << endl;
    }

    delete[] ptr;

    return 0;
}
