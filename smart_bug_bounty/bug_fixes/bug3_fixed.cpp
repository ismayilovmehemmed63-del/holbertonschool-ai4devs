#include <iostream>
#include <vector>
#include <string>
using namespace std;

int findMax(vector<int> arr) {
    int max = 0;
    for (int i = 0; i < (int)arr.size(); i++) {
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
    cout << greet("World") << endl;
    return 0;
}
