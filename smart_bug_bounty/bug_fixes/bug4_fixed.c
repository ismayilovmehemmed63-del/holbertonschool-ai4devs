#include <stdio.h>
#include <string.h>

void copy_input(char *input) {
    char buffer[10];
    strncpy(buffer, input, sizeof(buffer) - 1);
    buffer[sizeof(buffer) - 1] = 0;
    printf("Copied: %s", buffer);
}

int divide(int a, int b) {
    if (b == 0) {
        printf("Error: Division by zero");
        return -1;
    }
    return a / b;
}

int main() {
    char user_input[] = "Short";
    copy_input(user_input);

    int result = divide(10, 2);
    printf("Result: %d", result);

    int error = divide(10, 0);
    printf("Error result: %d", error);

    return 0;
}
