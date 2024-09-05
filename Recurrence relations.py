#include <stdio.h>

// Function to calculate T(n) using iteration method
int solveRecurrence(int n) {
    int T = 0; // Initialize T(n)
    int i = n;

    // Keep breaking n down until we reach the base case (T(1))
    while (i > 1) {
        T += i;     // Add n (or i at each step)
        i = i / 2;  // Divide i by 2 each step
    }

    // Add the base case, which is T(1) = 1
    T += 1;
    
    return T;
}

int main() {
    int n;
    
    // Take input for n
    printf("Enter a value for n: ");
    scanf("%d", &n);
    
    // Solve the recurrence relation using the iteration method
    int result = solveRecurrence(n);
    
    // Output the result
    printf("The result of the recurrence relation for T(%d) is: %d\n", n, result);

    return 0;
}
