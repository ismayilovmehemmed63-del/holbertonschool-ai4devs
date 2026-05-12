#include <stdio.h>
#include <string.h>

void copy_input(char *input) {
    char buffer[10];
    strcpy(buffer, input);
    printf("Copied: %s", buffer);
}

int divide(int a, int b) {
    return a / b;
}

int main() {
    char user_input[] = "This is a very long string that exceeds buffer";
    copy_input(user_input);

    int result = divide(10, 0);
    printf("Result: %d", result);

    return 0;
}
