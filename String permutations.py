#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Function to compare two strings lexicographically
int compareStrings(const void *a, const void *b) {
    return (*(char *)a - *(char *)b);
}

// Function to sort a string in place
void sortString(char *str) {
    size_t len = strlen(str);
    qsort(str, len, sizeof(char), compareStrings);
}

// Function to check if permutation of s1 can break permutation of s2
int canBreak(char *s1, char *s2) {
    size_t len = strlen(s1);

    // Sort both strings
    sortString(s1);
    sortString(s2);

    // Compare sorted strings
    for (size_t i = 0; i < len; i++) {
        if (s1[i] < s2[i]) {
            return 0; // s1 cannot break s2
        }
        if (s2[i] < s1[i]) {
            return 0; // s2 cannot break s1
        }
    }
    return 1; // At least one permutation can break the other
}

int main() {
    char s1[100], s2[100];

    printf("Enter the first string: ");
    scanf("%s", s1);

    printf("Enter the second string: ");
    scanf("%s", s2);

    if (strlen(s1) != strlen(s2)) {
        printf("Strings must be of the same length.\n");
        return 1;
    }

    if (canBreak(s1, s2)) {
        printf("Some permutation of '%s' can break some permutation of '%s' or vice versa.\n", s1, s2);
    } else {
        printf("No permutation of '%s' can break any permutation of '%s'.\n", s1, s2);
    }

    return 0;
}
