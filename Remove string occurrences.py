#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX_LENGTH 1000

// Function to remove the first occurrence of a character in a string
void remove_first_occurrence(char *s, char ch) {
    int length = strlen(s);
    int i, j;
    bool found = false;

    for (i = 0; i < length; ++i) {
        if (s[i] == ch) {
            found = true;
            // Shift all characters left by one position
            for (j = i; j < length - 1; ++j) {
                s[j] = s[j + 1];
            }
            s[length - 1] = '\0'; // Null-terminate the string
            break;
        }
    }
}

// Function to get the string before it becomes empty
void get_string_before_last_operation(char *s) {
    char temp[MAX_LENGTH];
    strcpy(temp, s); // Copy the original string
    int length = strlen(temp);
    bool is_empty;

    while (length > 0) {
        is_empty = true;

        // Try to remove the first occurrence of each character from 'a' to 'z'
        for (char ch = 'a'; ch <= 'z'; ++ch) {
            if (strchr(temp, ch) != NULL) {
                remove_first_occurrence(temp, ch);
                is_empty = false;
            }
        }

        if (is_empty) {
            // The string is empty, break the loop
            break;
        }
    }

    // Print the string before it becomes empty
    printf("String before last operation: %s\n", temp);
}

int main() {
    char s[MAX_LENGTH];

    printf("Enter the string: ");
    scanf("%s", s);

    get_string_before_last_operation(s);

    return 0;
}
