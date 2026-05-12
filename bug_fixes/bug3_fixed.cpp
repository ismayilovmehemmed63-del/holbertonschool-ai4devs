#include <iostream>
#include <vector>
#include <string>
using namespace std;

int findMax(vector<int> arr) {
    if (arr.empty()) {
        return -1;
    }
    int max = arr[0];
    for (int i = 1; i < (int)arr.size(); i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

string greet(string name) {
    string greeting = "Hello, " + name;
    cout << greeting << endl;
    return greeting;
}

int main() {
    vector<int> numbers = {3, 7, 1, 9, 4};
    cout << "Max: " << findMax(numbers) << endl;
    greet("World");
    vector<int> empty = {};
    cout << "Empty max: " << findMax(empty) << endl;
    return 0;
}
