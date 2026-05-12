#include <stdio.h>
#include <string.h>

void copy_input(char *input) {
    char buffer[100];
    strncpy(buffer, input, sizeof(buffer) - 1);
    buffer[sizeof(buffer) - 1] = '\0';
    printf("Copied: %s", buffer);
}

int divide(int a, int b) {
    if (b == 0) {
        printf("Error: Division by zero\n");
        return -1;
    }
    return a / b;
}

int main() {
    char user_input[] = "This is a very long string that exceeds buffer";
    copy_input(user_input);

    int result = divide(10, 0);
    printf("Result: %d\n", result);

    return 0;
}
