#include <iostream>
#include <vector>
#include <string>
using namespace std;

int findMax(vector<int> arr) {
    int max = 0;
    for (int i = 1; i <= arr.size(); i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

string greet(string name) {
    string greeting = "Hello, " + name;
    return greeting;
    cout << greeting << endl;
}

int main() {
    vector<int> numbers = {3, 7, 1, 9, 4};
    cout << "Max: " << findMax(numbers) << endl;
    cout << greet("World") << endl;
    return 0;
}
