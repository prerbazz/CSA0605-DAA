#include <stdio.h>
#include <time.h>

// Non-Recursive (Iterative) Factorial Function
long long factorial_iterative(int n) {
    long long result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

// Recursive Factorial Function
long long factorial_recursive(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial_recursive(n - 1);
}

int main() {
    int n;
    clock_t start, end;
    double time_taken_iterative, time_taken_recursive;
    
    printf("Enter a number to calculate its factorial: ");
    scanf("%d", &n);
    
    // Measure time for the iterative version
    start = clock();
    long long result_iterative = factorial_iterative(n);
    end = clock();
    time_taken_iterative = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Iterative factorial of %d is: %lld\n", n, result_iterative);
    printf("Time taken by iterative algorithm: %f seconds\n", time_taken_iterative);

    // Measure time for the recursive version
    start = clock();
    long long result_recursive = factorial_recursive(n);
    end = clock();
    time_taken_recursive = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Recursive factorial of %d is: %lld\n", n, result_recursive);
    printf("Time taken by recursive algorithm: %f seconds\n", time_taken_recursive);

    return 0;
}
