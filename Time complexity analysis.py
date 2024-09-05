#include <stdio.h>
#include <time.h>

// Example of O(1) Time Complexity
void constantTimeAlgorithm() {
    printf("O(1): This algorithm runs in constant time.\n");
}

// Example of O(n) Time Complexity
void linearTimeAlgorithm(int n) {
    printf("O(n): This algorithm runs in linear time.\n");
    for (int i = 0; i < n; i++) {
        // Doing some constant work
        printf(".");
    }
    printf("\n");
}

// Example of O(n^2) Time Complexity
void quadraticTimeAlgorithm(int n) {
    printf("O(n^2): This algorithm runs in quadratic time.\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            // Doing some constant work
            printf(".");
        }
        printf("\n");
    }
}

int main() {
    int n;
    printf("Enter the size of input (n): ");
    scanf("%d", &n);

    // Measure time for constant-time algorithm
    clock_t start = clock();
    constantTimeAlgorithm();
    clock_t end = clock();
    printf("Time taken by O(1): %lf seconds\n", (double)(end - start) / CLOCKS_PER_SEC);

    // Measure time for linear-time algorithm
    start = clock();
    linearTimeAlgorithm(n);
    end = clock();
    printf("Time taken by O(n): %lf seconds\n", (double)(end - start) / CLOCKS_PER_SEC);

    // Measure time for quadratic-time algorithm
    start = clock();
    quadraticTimeAlgorithm(n);
    end = clock();
    printf("Time taken by O(n^2): %lf seconds\n", (double)(end - start) / CLOCKS_PER_SEC);

    return 0;
}
