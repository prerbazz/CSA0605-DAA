#include <stdio.h>
#include <string.h>

#define ALPHABET_SIZE 26

void minimize_value(char *s) {
    int n = strlen(s);
    int freq[ALPHABET_SIZE] = {0}; // Frequency array for characters 'a' to 'z'
    int cost = 0;

    for (int i = 0; i < n; ++i) {
        if (s[i] == '?') {
            // Find a character to replace '?'
            for (char c = 'a'; c <= 'z'; ++c) {
                if (freq[c - 'a'] == 0) {
                    s[i] = c;
                    freq[c - 'a']++;
                    break;
                }
            }
        } else {
            // Update frequency
            int index = s[i] - 'a';
            // Add cost of this character appearing before the current position
            cost += freq[index];
            // Update frequency
            freq[index]++;
        }
    }

    // Output the minimized value of the string
    printf("Minimized value: %d\n", cost);
    printf("Resulting string: %s\n", s);
}

int main() {
    char s[100]; // Assuming input length is at most 100
    printf("Enter the string: ");
    scanf("%s", s);

    minimize_value(s);

    return 0;
}
